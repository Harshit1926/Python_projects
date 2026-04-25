# Face Recognition System (PyTorch + OpenCV)

A real-time face recognition system built using MobileNetV2, trained with transfer learning on the LFW dataset and fine-tuned on custom user data.

## Overview

This project demonstrates an end-to-end pipeline for face recognition:

* Face detection using OpenCV (Haarcascade)
* Feature extraction using a pretrained MobileNetV2 model
* Fine-tuning on a custom dataset
* Real-time prediction through webcam

A pretrained base model is provided, so users can directly fine-tune it on their own dataset without training from scratch.

---

## Features

* Real-time face detection and recognition
* Transfer learning using MobileNetV2
* Pretrained model trained on LFW dataset
* Fine-tuning on user-specific data
* Unknown face detection using confidence threshold

---

## Project Structure

```
face-recognition/
│
├── dataset/                  # Add your dataset here
├── models/
│   └── mobilenet_lfw.pth     # Pretrained base model
│
├── Fine_Tune.py               # Fine-tune model on your data
├── webcam.py                 # Real-time face recognition
└── README.md
```

---

## Dataset Preparation

This repository does not include a dataset.

You are expected to provide your own data in the following format:

```
dataset/
├── person1/
│   ├── img1.jpg
│   ├── img2.jpg
│
├── person2/
│   ├── img1.jpg
│   ├── img2.jpg
```

### Guidelines

* Use at least 20+ images per person
* The more images you provide, the better the model will perform
* Include variations:

  * lighting conditions
  * viewing angles
  * facial expressions

---

## Installation

Install dependencies:

```
pip install -r requirements.txt
```

---

## Usage

### 1. Fine-tune the model

```
python finetune.py
```

This will generate:

* `final_face_model.pth`
* `classes.json`

---

### 2. Run real-time recognition

```
python webcam.py
```

You will be prompted to start webcam testing.

---

## Model Details

* Backbone: MobileNetV2
* Pretraining: LFW (Labeled Faces in the Wild)
* Fine-tuning: Custom dataset

The provided model (`mobilenet_lfw.pth`) is trained to extract general facial features.
Users must fine-tune it for identity recognition.

---

## Notes

* High training accuracy on small datasets may indicate overfitting
* Real-world performance is a better indicator than training accuracy
* Increasing dataset size improves model performance significantly

---

## Future Improvements

* Face registration system (add new users dynamically)
* GUI or web-based interface
* Embedding-based recognition (FaceNet-style)

---

