# Dataset Instructions

This folder is intentionally left empty.

##  Add Your Own Data

Organize your dataset in the following structure:

dataset/
├── person1/
│   ├── img1.jpg
│   ├── img2.jpg
│
├── person2/
│   ├── img1.jpg
│   ├── img2.jpg

##  Guidelines

- Use at least **20+ images per person**
- **The more images you provide, the better the model will perform**
- Include variations:
  - Different lighting
  - Different angles
  - Facial expressions

##  Next Step

After adding your dataset, run:

python finetune.py