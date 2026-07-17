"""
AI-Powered Industrial Quality Assurance System
Week 7 & 8 Final Project

- Upload a steel surface image
- Detect defects using a trained YOLOv8 model
- Display detections with bounding boxes
- Send detections to a local LLM (Ollama + Llama 3.2) to generate an inspection report
- Show everything in a clean Streamlit UI
"""

import io
from datetime import date

import numpy as np
import requests
import streamlit as st
from PIL import Image
from ultralytics import YOLO

st.set_page_config(page_title="AI Industrial Quality Assurance", page_icon="🔍", layout="wide")


# ---------------------------------------------------------------------------
# Model loading
# ---------------------------------------------------------------------------
@st.cache_resource
def load_model(weights_path: str):
    return YOLO(weights_path)


def run_detection(model: YOLO, image: np.ndarray, conf: float):
    """Run YOLOv8 inference and return the annotated image + a list of detections."""
    results = model.predict(image, conf=conf, verbose=False)
    result = results[0]

    annotated_bgr = result.plot()          # ultralytics draws boxes/labels for us
    annotated_rgb = annotated_bgr[:, :, ::-1]

    names = result.names
    detections = []
    for box in result.boxes:
        cls_id = int(box.cls[0])
        confidence = float(box.conf[0])
        detections.append({"class": names[cls_id], "confidence": confidence})

    # Highest confidence first
    detections.sort(key=lambda d: d["confidence"], reverse=True)
    return annotated_rgb, detections


# ---------------------------------------------------------------------------
# LLM report generation (Ollama)
# ---------------------------------------------------------------------------
def build_prompt(detections: list, image_name: str) -> str:
    today = date.today().strftime("%d %B %Y")

    if detections:
        defect_lines = "\n".join(
            f"- {d['class']} ({d['confidence'] * 100:.0f}%)" for d in detections
        )
    else:
        defect_lines = "- No defects detected"

    prompt = f"""You are a quality assurance inspector at a steel manufacturing plant.
Write a professional inspection report based on these YOLOv8 defect detection results
for image "{image_name}".

Inspection Date: {today}
Detected Defects:
{defect_lines}

IMPORTANT RULES:
- Only use the exact defect names and confidence percentages listed above. Do not invent,
  estimate, or restate them as any other kind of measurement.
- Never state a percentage of "affected area," surface coverage, or any other numeric
  statistic that isn't one of the confidence scores given above — that data does not exist
  and must not be fabricated.
- If detections are empty or say "No defects detected", the report must say no defects
  were found, and Severity must be Low.

Severity guide (do not deviate):
- Low: no defects, or a single defect below 50% confidence
- Medium: one defect at 50%+ confidence, or multiple defects all below 50% confidence
- High: multiple defects with at least one at 50%+ confidence, or any single defect at 85%+ confidence

Respond using EXACTLY this format, with no extra commentary before or after it:

Inspection Report
Inspection Date: {today}

Detected Defects:
[list each defect with its confidence percentage, exactly as given above]

Summary:
[2-3 sentence plain-language summary of what was found, using only the defects and
confidence scores given above]

Severity:
[Low, Medium, or High — follow the severity guide above exactly]

Recommended Action:
[3-5 bullet points of concrete next steps]
"""
    return prompt


def query_ollama(prompt: str, model_name: str = "llama3.2", host: str = "http://localhost:11434"):
    """Call a local Ollama server. Returns the generated text, or None if unreachable."""
    try:
        response = requests.post(
            f"{host}/api/generate",
            json={"model": model_name, "prompt": prompt, "stream": False},
            timeout=120,
        )
        response.raise_for_status()
        return response.json().get("response", "").strip()
    except requests.exceptions.ConnectionError:
        return None
    except Exception as exc:  # noqa: BLE001
        return f"Error while generating report: {exc}"


# ---------------------------------------------------------------------------
# UI
# ---------------------------------------------------------------------------
st.title("🔍 AI-Powered Industrial Quality Assurance")
st.caption("Upload a steel surface image to detect defects and generate an AI inspection report.")

with st.sidebar:
    st.header("Settings")
    weights_path = st.text_input("YOLOv8 weights path", value="best.pt")
    conf_threshold = st.slider("Confidence threshold", 0.0, 1.0, 0.25, 0.05)
    ollama_model = st.text_input("Ollama model", value="llama3.2")
    st.markdown("---")
    st.markdown(
        "**Before running:**\n"
        "1. Install & start Ollama: `ollama serve`\n"
        "2. Pull the model once: `ollama pull llama3.2`\n"
        "3. Put your trained `best.pt` in this folder (or point the path above to it)"
    )

uploaded_file = st.file_uploader("Upload a steel surface image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert("RGB")

    try:
        model = load_model(weights_path)
    except Exception as exc:  # noqa: BLE001
        st.error(f"Could not load model weights at '{weights_path}': {exc}")
        st.stop()

    col1, col2 = st.columns(2)
    with col1:
        st.subheader("Original Image")
        st.image(image, use_container_width=True)

    with st.spinner("Detecting defects..."):
        annotated_img, detections = run_detection(model, np.array(image), conf_threshold)

    with col2:
        st.subheader("Detected Defects")
        st.image(annotated_img, use_container_width=True)

    st.markdown("---")
    st.subheader("Detection Results")
    if detections:
        for d in detections:
            st.write(f"- **{d['class']}** ({d['confidence'] * 100:.0f}%)")
    else:
        st.write("No defects detected above the confidence threshold.")

    st.markdown("---")
    st.subheader("AI-Generated Inspection Report")

    with st.spinner("Generating report with local LLM (Ollama)..."):
        prompt = build_prompt(detections, uploaded_file.name)
        report = query_ollama(prompt, model_name=ollama_model)

    if report is None:
        st.error(
            "Could not connect to Ollama at http://localhost:11434. "
            "Make sure it's running (`ollama serve`) and the model is pulled "
            f"(`ollama pull {ollama_model}`)."
        )
    else:
        st.text(report)
        st.download_button("Download Report (.txt)", report, file_name="inspection_report.txt")

else:
    st.info("Upload an image to get started.")