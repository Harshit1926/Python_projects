# CAMERA AND VIDEO RECORDER

A command-line tool built with OpenCV to capture photos and record videos using your webcam. It supports both internal and external cameras, offers user-friendly prompts, and ensures smooth resource cleanup.

# FEATURES

1. Choose between internal and external webcams

2. Interactive mode selection for photo capture or video recording

3. Live camera feed with preview windows

4. Save photographs on keypress (s)

5. Record videos with specified filename and codec (XVID)

6. Real-time feedback and graceful exit options

7. Robust input validation

# REQUIREMENTS

1. Python 3.x

2. OpenCV (cv2)

Install OpenCV using pip:
Open your Command Prompt or terminal and run:

pip install opencv-python

# HOW TO USE

1. Run the script in a python environment

2. Camera Selection:
    - Type 0 for internal webcam
    - Type 1 for external webcam
    - Choose Mode:
    - Type 1 to capture a photograph
    - Type 2 to record a video

# KEY CONTROLS 

  # Photograph Mode
    - Press s to save the image
    - Press e to exit without saving

  # Video Mode:
    - Press q to stop recording and save the file

# OUTPUT

1. Photos are saved in the same directory as the script
2. Videos are saved in .avi format using the XVID codec

# AUDIO DISCLAIMER

This tool does not record audio. It captures only the video stream from the selected webcam.





