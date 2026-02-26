# import necessary libraries
import torch
import torch.nn as nn
import torch.optim as optim
from torchvision.datasets import ImageFolder
from torchvision import transforms
from torch.utils.data import DataLoader
from torchvision import models
import cv2
from PIL import Image

# Loading data and preprocessing
transform_train = transforms.Compose([
    transforms.Resize((224,224)),
    transforms.RandomHorizontalFlip(),
    transforms.RandomRotation(10),
    transforms.ColorJitter(brightness=0,contrast=0.2),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5], std=[0.5,0.5,0.5])
])
transform_test=transforms.Compose([
    transforms.Resize((224,224)),
    transforms.ToTensor(),
    transforms.Normalize(mean=[0.5,0.5,0.5],std=[0.5,0.5,0.5])
])

train_data = ImageFolder(root='/enter your file root', transform=transform_train)

train_loader = DataLoader(train_data, batch_size=64, shuffle=True)

# Defining the class
class FaceRecognizer(nn.Module):
    def __init__(self, num_classes):
        super(FaceRecognizer, self).__init__()
        self.mobile = models.mobilenet_v2(pretrained=True)   
        self.mobile.classifier[1] = nn.Linear(self.mobile.classifier[1].in_features, num_classes)

    def forward(self, x):
        return self.mobile(x)

num_classes = len(train_data.classes)
model = FaceRecognizer(num_classes)

# device setup
device = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
model.to(device)
for name,params in model.mobile.features.named_parameters():
    params.requires_grads=False


loss_function = nn.CrossEntropyLoss()
optimizer = optim.Adam(model.mobile.classifier.parameters(), lr=0.001)

# training loop
epochs = 5
for epoch in range(epochs):
    running_loss = 0
    total,correct=0,0
    for images, labels in train_loader:
        images, labels = images.to(device), labels.to(device)
        outputs = model(images)
        loss = loss_function(outputs, labels)
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        running_loss += loss.item()
        _,predicted=torch.max(outputs,1)
        total+=labels.size(0)
        correct+=(predicted==labels).sum().item()
    epoch_accuracy=100*correct/total
    print(f"Epoch [{epoch+1}/{epochs}], Loss: {running_loss/len(train_loader):.4f}, Accuracy={epoch_accuracy:.2f}%")


model.eval()
classes=train_data.classes
cap=cv2.VideoCapture(0)
print("To Stop Video press 'q'")
while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame_RGB=cv2.cvtColor(frame,cv2.COLOR_BGR2RGB)
    pil_image=Image.fromarray(frame_RGB)

    input_tensor=transform_test(pil_image).unsqueeze(0).to(device)
# unsqueeze(0) add extra dimension to the image as pytorch accept images in batch not single image
    with torch.no_grad():
        outputs=model(input_tensor)
        _,prediction=torch.max(outputs,1)
        label=classes[prediction.item()]
    cv2.putText(frame, f"Prediction: {label}", (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)
    
    cv2.imshow("Live image",frame)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
print(train_data.classes)
print(train_data.class_to_idx)
print(len(train_data))

torch.save(model.state_dict(), "mobilenet_face.pth")