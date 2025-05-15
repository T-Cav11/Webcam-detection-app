Motion Detection Security Camera

A Python application that uses your webcam to detect motion, capture images when movement is detected, and automatically send email notifications with the captured images.

Overview

This application turns any computer with a webcam into a basic security system. It continuously monitors for movement using computer vision techniques, and when motion is detected, it captures a series of images. Once the motion stops, the system automatically sends an email notification with one of the captured images attached, providing a simple but effective security monitoring solution.

Features

Real-time Motion Detection: Uses computer vision to identify movement in the webcam feed

Automatic Image Capture: Saves images when motion is detected

Email Notifications: Sends email alerts with captured images

Efficient Storage Management: Automatically cleans up images after sending

Visual Monitoring: Displays processed video feeds with motion highlighting

Low Resource Usage: Optimized for running on standard hardware

How It Works

The application captures a reference frame when first started

It continuously compares new frames with the reference frame

When significant differences (motion) are detected:

The moving object is highlighted with a green rectangle
Images are captured and saved


When motion stops, an email is sent with one of the captured images

The images folder is cleaned to save storage space

Requirements

Python 3.6+

OpenCV (cv2)

A webcam or camera connected to your computer

Email account for sending notifications