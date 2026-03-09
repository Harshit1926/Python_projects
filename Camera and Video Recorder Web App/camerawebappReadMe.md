# Flask Camera Capture Web App

A simple **web-based camera application** built with **Flask and OpenCV** that allows users to select a camera, choose between **photo or video mode**, and capture images or record videos using their webcam.

The application provides a browser-based interface to control the camera while OpenCV handles the actual capture and recording functionality.

---

## Features

* Select **Inbuilt or External Camera**
* Choose between **Photo Mode** and **Video Mode**
* Capture images using the webcam
* Record videos using the webcam
* Real-time camera preview using OpenCV
* User-friendly interface with flash messages
* Session-based user selections

---

## Tech Stack

### Backend

* Python
* Flask
* OpenCV

### Frontend

* HTML
* CSS *(AI-assisted styling)*
* JavaScript *(AI-assisted implementation for UI interaction and form handling)*

---

## How the Application Works

1. The user selects a **camera source** (inbuilt or external).
2. The user chooses between **photo mode** or **video mode**.
3. The application opens the selected camera using OpenCV.
4. Depending on the selected mode:

   * **Photo Mode**

     * Live camera feed is displayed.
     * Press **C** to capture a photo.
     * Press **Q** to quit.
   * **Video Mode**

     * Recording starts with live preview.
     * Press **Q** to stop recording.
5. Captured photos or videos are saved with a **timestamp-based filename**.

---

## Project Structure

```
project-folder/
│
├── camera&recorder.py
│
├── templates/
│   ├── camera.html
│   ├── photovideo.html
│   └── capture.html   
│
└── README.md
```

---

## Installation

### 1 Clone the repository

```
git clone https://github.com/Harshit1926/Python_projects.git
```

### 2 Navigate to the project folder

```
cd Camera and Video Recorder Web App
```

### 3 Install required libraries

```
pip install flask opencv-python
```

### 4 Run the application

```
python app.py
```

### 5 Open the browser

The application will automatically open at:

```
http://127.0.0.1:5000
```

---

## Controls

### Photo Mode

| Key | Function      |
| --- | ------------- |
| C   | Capture Photo |
| Q   | Quit Camera   |

### Video Mode

| Key | Function       |
| --- | -------------- |
| Q   | Stop Recording |

---

## Output

* Photos are saved as:

```
YYYY-MM-DD_HH-MM-SS.jpg
```

* Videos are saved as:

```
YYYY-MM-DD_HH-MM-SS.avi
```

---

## Future Improvements

* Add **browser-based capture instead of keyboard controls**
* Add **live video streaming inside the webpage**
* Add **download option for captured media**
* Integrate **face detection or recognition**
* Deploy the application on a cloud platform

---

## Acknowledgment

*Some parts of the frontend styling (CSS) and JavaScript logic were developed with AI-assisted support to improve the user interface and enhance usability.*

---

## Author

**Harshit Malhotra**

GitHub: https://github.com/Harshit1926
LinkedIn: https://www.linkedin.com/in/harshit-malhotra-868664377/
