# =========================
# 1. IMPORTS
# =========================
import torch
import torch.nn as nn
from torchvision import transforms, models
import cv2
from PIL import Image
import json

# =========================
# 2. LOAD CLASS NAMES
# =========================
with open("classes.json", "r") as f:
    classes = json.load(f)

# =========================
# 3. MODEL DEFINITION
# =========================
class FaceRecognizer(nn.Module):
    def __init__(self, num_classes):
        super().__init__()
        self.mobile = models.mobilenet_v2(pretrained=False)
        self.mobile.classifier[1] = nn.Linear(
            self.mobile.classifier[1].in_features,
            num_classes
        )

    def forward(self, x):
        return self.mobile(x)

model = FaceRecognizer(len(classes))
model.load_state_dict(torch.load("final_face_model.pth", map_location="cpu"))
model.eval()

# =========================
# 4. TRANSFORMS
# =========================
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.ToTensor(),
    transforms.Normalize([0.5]*3, [0.5]*3)
])

# =========================
# 5. HAARCASCADE FACE DETECTOR
# =========================
face_cascade = cv2.CascadeClassifier(
    cv2.data.haarcascades + "haarcascade_frontalface_default.xml"
)

# =========================
# 6. WEBCAM START
# =========================
cap = cv2.VideoCapture(0)

print("Press 'q' to exit")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    for (x, y, w, h) in faces:
        face = frame[y:y+h, x:x+w]

        # Convert to PIL
        rgb = cv2.cvtColor(face, cv2.COLOR_BGR2RGB)
        pil_img = Image.fromarray(rgb)

        # Transform
        input_tensor = transform(pil_img).unsqueeze(0)

        # Prediction
        with torch.no_grad():
            outputs = model(input_tensor)
            probs = torch.nn.functional.softmax(outputs, dim=1)
            confidence, pred = torch.max(probs, 1)

            label = classes[pred.item()]
            conf = confidence.item()

        #  Unknown face detection
        if conf < 0.6:
            label_text = "Unknown"
        else:
            label_text = f"{label} ({conf:.2f})"

        # Draw box
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,255,0), 2)
        cv2.putText(frame, label_text, (x, y-10),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0,255,0), 2)

    cv2.imshow("Face Recognition", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()