# Invisibility Cloak using OpenCV (Fun Project) 🧙‍♂️

*Ever wondered what it would feel like to have Harry Potter's invisibility cloak?* 👀
This project recreates a simple version of that effect using Python, OpenCV, and Computer Vision.

The program detects a specific cloak color (red, green, or blue) and replaces it with the captured background, creating the illusion that the cloak has become invisible.

This was created as a small fun experiment while learning computer vision concepts.

# How It Works 🎥

The program starts and captures the background for a few seconds.

Each frame from the webcam is converted from BGR to HSV color space.

A color mask is created to detect the cloak color.

Morphological operations remove noise from the mask.

The cloak area is replaced with the background image.

The result creates the illusion that the cloak is invisible.

# Technologies Used 🛠️

Python

OpenCV

NumPy

Computer Vision (HSV Color Detection)

# Installation 📦

Install the required libraries:

pip install opencv-python numpy
▶️ Running the Project

Run the Python script:

python Invisible_cloak.py

The program will ask for webcam selection:

Enter 0 for internal webcam and 1 for external webcam

Then select cloak color:

Enter the color of the cloak (red, green, blue)

Example:

Enter 0 for internal webcam and 1 for external webcam: 0
Enter the color of the cloak (red, green, blue): red
🎮 Controls

Press:

Q → Quit the application

# Project Structure 📂
invisibility-cloak/
│
├── invisibility_cloak.py
└── README.md
🎯 Features

Supports internal and external webcams

Detects Red, Green, or Blue cloak

Real-time color detection using HSV

Uses OpenCV masking and background replacement

Simple and interactive

# Tips for Best Results ⚠️

Use a solid colored cloth

Make sure the background remains stable

Avoid wearing clothes that match the cloak color

Good lighting improves color detection accuracy

# Why I Made This 😄

I came across the idea of an Invisibility Cloak project online and thought it looked really fun.
So I decided to recreate it myself using Python and OpenCV while experimenting with computer vision and real-time video processing.

This project helped me understand concepts like color detection, masking, and background replacement in a simple and practical way.

# Possible Improvements 🚀

Automatic cloak color detection

Better noise reduction

Support for multiple cloak colors

GUI interface for easier control