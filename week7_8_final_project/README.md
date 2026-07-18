# Week 7 & 8: LLM Integration & Deployment

## Topics Covered
- Building a Streamlit web app
- Integrating a trained YOLOv8 model into the app
- Using a local LLM with Ollama (Llama 3.2)
- Generating an inspection report from the detected defects

## Learning Outcome
I learned how to connect a trained YOLOv8 model to a Streamlit app so it can detect defects on an uploaded image and show the bounding boxes. I also learned how to call a local LLM through Ollama to turn the detection results into a written inspection report.

## AI-Powered Industrial Quality Assurance System

## How to Run
1. Install requirements: `pip install -r requirements.txt`
2. Install Ollama and pull the model: `ollama pull llama3.2`
3. Make sure Ollama is running (`ollama serve`)
4. Put `best.pt` in this folder
5. Run the app: `streamlit run app.py`
6. Upload a steel surface image and it will show the detections and generate a report

## Files
- app.py
- requirements.txt
- best.pt (trained YOLOv8 model)
