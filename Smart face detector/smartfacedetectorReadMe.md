# SMART FACE DETECTOR

An interactive OpenCV tool that detects faces, eyes, and smiles in real-time using your webcam. When a smile is spotted, the system automatically captures a photo and saves it with a timestamp. You’ll find all necessary detection files included for a plug-and-play experience.

# FEATURES

1. Real-time face, eye, and smile detection

2. Auto-capture when a smile is detected

3. Built-in cooldown timer (default: 20 seconds) between snapshots

4. Dynamic overlays for detected features

5. Timestamped filenames for saved photos

6. Compatible with internal and external webcams

7. Exit with grace by pressing q

# REQUIREMENTS

1. Python 3.x
2. OpenCV (cv2)
3. Built-in modules: time, os

Installation
pip install opencv-python

 # HOW TO USE

1. Run the script:

2. Select Webcam Input:

3. 0 for internal

4. 1 for external

5. Detection & Capture:

6. Smile and let the tool snap your photo!

7. Watch for overlays like Eyes Detected and Smile Detected

8. Quit:
    - Press q to exit the window

# OUTPUT

1. Photos are saved in the same directory as the script

2. Filename format: photo_YYYY-MM-DD HH MM SS.jpg

# DETECTION FILES PROVIDED

All necessary Haarcascade classifiers are included in the project folder alongside the Python file and README.
These files must either be in the same directory or accessible via the correct path. 




