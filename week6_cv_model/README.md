# Week 6: CV Model

## Topics Covered
- Object detection fundamentals with YOLOv8
- Setting up a YOLOv8 training pipeline in Google Colab (GPU runtime)
- Preparing a custom dataset (NEU-DET steel surface defects) with `data.yaml` and YOLO-format labels
- Training and comparing multiple model sizes (nano, small, medium)
- Evaluating a trained model: Precision, Recall, mAP@50, mAP@50-95
- Reading training curves and confusion matrices
- Running inference and visualizing sample predictions with bounding boxes

## Learning Outcome
I learned how to train a YOLOv8 object detection model end-to-end: preparing the dataset, running training across different model sizes, and evaluating results using standard object detection metrics. I also learned how model size affects training time and detection quality, and how to interpret a confusion matrix and per-class confidence scores to judge where a model is weaker (e.g. harder-to-detect defect classes like crazing) versus stronger (e.g. scratches).

## Files
- Week6_CV_Model_YOLOv8 (3).ipynb
- best.pt (best trained model weights)
