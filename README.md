# 🤖 Multi-Modal AI System for Industrial Quality Assurance

## Overview
This repository contains my work and learning progress for the **Multi-Modal AI System for Industrial Quality Assurance** project under the Summer of Code (SoC) program.

The goal of this project is to understand and build AI systems that can analyze multiple types of data for industrial quality assurance tasks. Throughout the project, I am learning the fundamentals of Python, Machine Learning, Deep Learning, Computer Vision, and Large Language Models (LLMs).

---

## 📚 Progress Summary

### Week 1: Python Basics 🐍
* Set up Python development environment.
* Learned Python syntax, variables, data types, lists, dictionaries, loops, and functions.
* Practiced writing basic Python programs.
* Studied introductory Machine Learning concepts.

### Week 2: Machine Learning Basics 📊
* Learned basic data handling and analysis using Pandas.
* Learned the fundamentals of Machine Learning.
* Studied supervised and unsupervised learning.
* Explored model evaluation concepts, overfitting, underfitting, and bagging.

### Week 3: Deep Learning & CNN 🧠
* Learned the fundamentals of Deep Learning and neural networks.
* Studied activation functions, forward propagation, backpropagation, and gradient descent.
* Explored the basic concepts behind Convolutional Neural Networks (CNNs).

### Week 4: Introduction to LLMs 💬
* Learned the basics of Large Language Models (LLMs).
* Explored how LLMs understand and generate text.
* Completed introductory tutorials on working with LLMs.

### Week 5: EDA (Exploratory Data Analysis) 📈
* Learned Exploratory Data Analysis (EDA) in Python.
* Completed a tutorial on Data Cleaning.
* Practiced working through notebooks cell by cell in Google Colab.

### Week 6: CV Model 🖼️
* Learned object detection with YOLOv8.
* Trained a YOLOv8 model on the NEU-DET (steel surface defects) dataset.
* Compared nano, small, and medium model sizes.
* Evaluated the trained model using Precision, Recall, mAP@50, and mAP@50-95.
* Saved the best trained model as `best.pt`.

### Week 7 & 8: LLM Integration & Deployment 🚀
* Built a Streamlit web application.
* Integrated the trained YOLOv8 model into the app for defect detection.
* Learned to use a local LLM (Llama 3.2) with Ollama.
* Generated AI-powered inspection reports based on detected defects.
* Completed the final project: an AI-powered Industrial Quality Assurance system that uploads a steel surface image, detects defects with bounding boxes, and generates a professional inspection report using a local LLM.

---

## 📂 Repository Structure
```text
├── Week-1-Python-Basics/
├── Week-2-ML-Basics/
├── Week-3-Deep-Learning-CNN/
├── Week-4-Intro-to-LLM/
├── week-5-EDA (Exploratory Data Analysis)/
├── week-6-CV Model/
└── week7_8_final_project-LLM Integration & Deployment/
```

## 🛠️ Technologies Explored
* Python
* Pandas
* Machine Learning
* Deep Learning
* CNNs
* Large Language Models (LLMs)
* YOLOv8 (Computer Vision / Object Detection)
* Streamlit
* Ollama (local LLM deployment)

## 🚀 Current Status
Completed all 8 weeks of the learning roadmap, including the final project — an AI-powered Industrial Quality Assurance system combining a trained YOLOv8 defect detection model with a local LLM (Llama 3.2 via Ollama) inside a Streamlit web app.
