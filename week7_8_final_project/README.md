# AI-Powered Industrial Quality Assurance System

Final project for Weeks 7 & 8: a Streamlit app that detects steel surface
defects with a trained YOLOv8 model and generates a professional inspection
report using a local LLM (Ollama + Llama 3.2).

## Features

- Upload a steel surface image
- Detect defects (crazing, inclusion, patches, pitted_surface,
  rolled-in_scale, scratches) using your trained YOLOv8 model
- View detections with bounding boxes drawn on the image
- Auto-generate a formatted inspection report (summary, severity,
  recommended actions) via a local LLM
- Download the report as a text file

## Setup

### 1. Clone this repo

```bash
git clone <your-repo-url>
cd <your-repo-folder>
```

### 2. Install Python dependencies

```bash
python -m venv venv
source venv/bin/activate   # on Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Install Ollama and pull Llama 3.2

Download Ollama from https://ollama.com, then:

```bash
ollama serve            # starts the local LLM server (leave this running)
ollama pull llama3.2    # one-time download of the model
```

### 4. Add your trained model

Copy your `best.pt` (from the Week 6 YOLOv8 training notebook) into this
project folder. The app defaults to looking for `best.pt` in the current
directory — you can change the path in the sidebar if it's elsewhere.

### 5. Run the app

```bash
streamlit run app.py
```

This opens the app in your browser at `http://localhost:8501`.

## Usage

1. Upload a steel surface image (`.jpg`/`.jpeg`/`.png`)
2. The app runs YOLOv8 inference and shows the annotated image side by side
   with the original
3. Detected defects and their confidence scores are listed below
4. The app sends those detections to Ollama, which writes a structured
   inspection report (Summary, Severity, Recommended Action)
5. Download the report with the button at the bottom

## Project Structure

```
.
├── app.py              # Streamlit application
├── best.pt              # Your trained YOLOv8 weights (add this yourself)
├── requirements.txt
└── README.md
```

## Submission Checklist

- [ ] Public GitHub repository with this code (`app.py`, `requirements.txt`,
      `README.md`)
- [ ] Trained model weights (`best.pt`) included in the repo or linked
      (use Git LFS if it's large)
- [ ] Short demo video (2–5 minutes) showing:
  - Uploading an image
  - Detection + bounding boxes appearing
  - The generated inspection report
- [ ] Submit via the assignment's final submission link
