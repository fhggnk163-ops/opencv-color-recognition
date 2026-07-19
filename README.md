# OpenCV Color Recognition

## Project Description

This project is a real-time color recognition system using OpenCV and Python.

The program uses the laptop camera to detect different colors and identify them in real time. It can recognize:

- Green
- Red
- Blue
- Yellow

When a color is detected, the program draws a rectangle around the object and displays the color name.

---

## Technologies Used

- Python 3.11
- OpenCV
- NumPy
- Anaconda
- Visual Studio Code

---

## Project Requirements

- Python installed through Anaconda
- Webcam
- OpenCV library
- NumPy library

---

## Installation

### 1. Create Anaconda Environment

Create a new environment:

```bash
conda create -n opencv_env python=3.11


conda activate opencv_env



Activate the environment:

conda activate opencv_env
2. Install Required Libraries

Install OpenCV and NumPy:

pip install -r requirements.txt
Running the Project

Run the program using:

python color_recognition.py

A camera window will open and the program will start detecting colors.

Press:

Q

to close the program.

How It Works
Capture video from the webcam.
Convert the image from BGR color space to HSV.
Apply color ranges to detect specific colors.
Create a mask for each detected color.
Find objects using contours.
Draw a bounding box around detected objects.
Display the detected color name.
Project Structure
opencv-color-recognition
│
├── color_recognition.py
├── requirements.txt
├── README.md
└── images
Author

Ahmed Fahd Khosim