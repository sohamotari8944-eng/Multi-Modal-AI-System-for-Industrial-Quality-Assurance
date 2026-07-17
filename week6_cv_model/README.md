# Week 6: CV Model

## Dataset

| Dataset | Link | Notes |
|---|---|---|
| NEU-DET (steel surface defects) | https://www.kaggle.com/datasets/zymzym/neu-yolo | Use YOLOv8 model, experiment with nano, small, medium, and large variants to get the best output. |

## Tasks

- Train a YOLOv8 model using the provided dataset.
- Save the best model (`best.pt`).
- Report the following metrics:
  - Precision
  - Recall
  - mAP@50
  - mAP@50-95
- Include screenshots of:
  - Training curves
  - Confusion matrix
  - Sample predictions

## Metric Thresholds

| Metric | Good | Excellent |
|---|---|---|
| Precision | ≥ 0.80 | ≥ 0.90 |
| Recall | ≥ 0.60 | ≥ 0.75 |
| mAP@50 | ≥ 0.75 | ≥ 0.85 |
| mAP@50-95 | ≥ 0.40 | ≥ 0.50 |

**Deadline:** 7th July, 2026 [Hard Deadline]
