# =========================
# 1. IMPORTS
# =========================
import os
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision.datasets import ImageFolder
from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision import models
import json

# =========================
# 2. DEVICE SETUP
# =========================
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using device:", device)

# =========================
# 3. DATA TRANSFORMS (BALANCED AUGMENTATION)
# =========================
transform = transforms.Compose([
    transforms.Resize((224, 224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(15),
    transforms.ColorJitter(brightness=0.2, contrast=0.2),
    transforms.ToTensor(),
    transforms.Normalize([0.5] * 3, [0.5] * 3)
])

# =========================
# 4. LOAD DATASET
# =========================
data_path = "dataset"

if not os.path.exists(data_path):
    raise FileNotFoundError("Dataset folder not found. Please create 'dataset/' and add images.")

train_data = ImageFolder(root=data_path, transform=transform)

train_loader = DataLoader(
    train_data,
    batch_size=16,
    shuffle=True
)

print("Classes:", train_data.classes)

# =========================
# 5. MODEL DEFINITION
# =========================
class FaceRecognizer(nn.Module):
    def __init__(self, num_classes):
        super().__init__()

        # Load base MobileNetV2 architecture
        self.mobile = models.mobilenet_v2(pretrained=False)

        # Replace classifier with dropout + new linear layer
        self.mobile.classifier = nn.Sequential(
            nn.Dropout(0.5),
            nn.Linear(1280, num_classes)
        )

    def forward(self, x):
        return self.mobile(x)

model = FaceRecognizer(len(train_data.classes))

# =========================
# 6. LOAD PRETRAINED LFW WEIGHTS
# =========================
MODEL_PATH = os.path.join("models", "mobilenet_lfw.pth")

if not os.path.exists(MODEL_PATH):
    raise FileNotFoundError("Pretrained model not found at models/mobilenet_lfw.pth")

state_dict = torch.load(MODEL_PATH, map_location=device)

# Remove classifier weights safely (to avoid size mismatch)
keys_to_remove = [k for k in state_dict.keys() if "classifier" in k]
for k in keys_to_remove:
    state_dict.pop(k)

# Load remaining weights
model.load_state_dict(state_dict, strict=False)

model = model.to(device)

# =========================
# 7. PARTIAL FREEZING OF LAYERS
# =========================
# Freeze early layers (general feature extractors)
for param in model.mobile.features[:15].parameters():
    param.requires_grad = False

# Unfreeze deeper layers (task-specific learning)
for param in model.mobile.features[15:].parameters():
    param.requires_grad = True

# =========================
# 8. LOSS FUNCTION AND OPTIMIZER
# =========================
criterion = nn.CrossEntropyLoss()

optimizer = optim.Adam(
    filter(lambda p: p.requires_grad, model.parameters()),
    lr=1e-4
)

# =========================
# 9. TRAINING LOOP
# =========================
epochs = 6

for epoch in range(epochs):
    model.train()
    total = 0
    correct = 0
    running_loss = 0

    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)

        outputs = model(images)
        loss = criterion(outputs, labels)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        running_loss += loss.item()

        _, predicted = torch.max(outputs, 1)
        total += labels.size(0)
        correct += (predicted == labels).sum().item()

    accuracy = 100 * correct / total
    avg_loss = running_loss / len(train_loader)

    print(f"Epoch {epoch + 1}/{epochs} | Loss: {avg_loss:.4f} | Accuracy: {accuracy:.2f}%")

# =========================
# 10. SAVE MODEL AND CLASSES
# =========================
torch.save(model.state_dict(), "final_face_model.pth")

with open("classes.json", "w") as f:
    json.dump(train_data.classes, f)

print("Training complete. Model and class labels saved.")