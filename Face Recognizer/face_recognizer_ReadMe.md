# FACE RECOGNIZER (MobileNetV2)

A command-line tool built with **PyTorch**, **Torchvision**, and **OpenCV** to recognize faces in real-time using a webcam.  
It leverages transfer learning with MobileNetV2 pretrained on ImageNet, retrains a classifier on a small dataset, and performs live inference with predictions overlayed on video.

---

# FEATURES

1. Uses **MobileNetV2** pretrained on ImageNet for feature extraction  
2. Freezes backbone layers to prevent overfitting on small datasets  
3. Trains a custom classifier for identity recognition  
4. Real-time webcam inference with predictions displayed on video feed  
5. Supports multiple identities (3 classes in current dataset)  
6. Saves trained model (`mobilenet_face.pth`) for reuse  
7. Current best training accuracy: **77.14%**  
8. Project is **still in progress** and will be updated to achieve better results  

---

# REQUIREMENTS

1. Python 3.x  
2. PyTorch  
3. Torchvision  
4. OpenCV (`cv2`)  
5. Pillow (`PIL`)  

Install dependencies using pip:
```bash
pip install torch torchvision opencv-python pillow