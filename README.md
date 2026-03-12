# Facial Recognition Attendance System

## Overview
Automated attendance management system using real-time 
facial recognition. Developed as a major project during 
undergraduate studies (BTech, KIIT University, 2024).

## What It Does
Replaces manual attendance tracking with automated 
face detection and recognition using a live webcam 
feed. Recognized students are logged automatically 
into a MySQL database.

## Technical Stack
- Python (OpenCV, NumPy, Pillow)
- LBPH (Local Binary Pattern Histogram) algorithm 
  for facial recognition
- Haar Cascade Classifier for face detection
- Tkinter (GUI)
- MySQL (attendance and student records storage)

## Key Features
- Real-time face detection from live video feed
- Student registration and model training via GUI
- Automated attendance logging to MySQL database
- CSV export of attendance records
- 90%+ recognition accuracy under normal 
  lighting conditions

## System Architecture
```
Live Video Feed (OpenCV)
        ↓
Face Detection (Haar Cascade)
        ↓
Face Recognition (LBPH Algorithm)
        ↓
Attendance Logging (MySQL Database)
        ↓
Export / View (Tkinter GUI)
```

## How to Run

### Prerequisites
```bash
pip install opencv-python numpy pillow 
pip install mysql-connector-python
```

### Setup
```bash
# 1. Clone the repository
git clone https://github.com/beepin6409/
facial-recognition-attendance

# 2. Set up MySQL database
# Run the schema SQL file provided in /database

# 3. Launch the application
python main.py
```

## Results
- 90%+ accuracy under normal lighting conditions
- Slight accuracy reduction under poor lighting 
  or with accessories (glasses, masks)
- Successfully handles multiple simultaneous 
  face detections

## Limitations & Future Improvements
- LBPH algorithm susceptible to poor lighting — 
  CNN-based approach would improve robustness
- Currently local MySQL only — cloud storage 
  would improve scalability
- No mobile integration yet

## Context
Undergraduate Major Project — BTech Computer Science,  
Kalinga Institute of Industrial Technology (KIIT), 2024  
```


NOT PINNED (background evidence):
└── facial-recognition-attendance
    ✓ Complete — Undergraduate project
