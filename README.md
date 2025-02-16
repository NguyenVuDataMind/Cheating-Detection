Cheating Detection on E-learning System

Group 01

Class 48K29.2, University of Economics, Da Nang

Project Overview

This project focuses on detecting cheating behaviors in an e-learning environment using YOLO and Heroku for image processing, with MongoDB to store results.

Technologies Used

Heroku: Handles image processing.

MongoDB: Stores detection results.

YOLO 11 (Ultralytics) for model training:

Advanced feature extraction: YOLO11 utilizes an improved backbone and neck architecture to enhance object detection accuracy and handle complex tasks.

Optimized for efficiency and speed: YOLO11 introduces refined architectural designs and optimized training processes, offering faster inference speeds while maintaining an optimal balance between accuracy and performance.

Higher accuracy with fewer parameters: YOLO11m achieves a higher mean Average Precision (mAP) on the COCO dataset while using 22% fewer parameters than YOLOv8m, making computations more efficient without sacrificing accuracy.

Adaptability across environments: YOLO11 can be seamlessly deployed across various environments, including edge devices, cloud platforms, and NVIDIA GPU-supported systems, ensuring maximum flexibility.

Wide range of supported tasks: YOLO11 is designed for multiple computer vision challenges, including object detection, instance segmentation, image classification, pose estimation, and oriented object detection (OBB).

Deployment Considerations

Heroku slug size limit (<500MB)

Installing ultralytics directly in requirements.txt may cause errors.

Heroku memory constraints (>1GB)

Requires a web dyno performance tier (must have a billing history on Heroku).

Note: Heroku web dynos are not always free; free plans do not run 24/7.

Private keys in server.py should be configured separately on Heroku.

Custom browser instance is required to send requests to the Heroku server for processing and fraud detection.

Important: Do not use .pt models, as inference time will be too long. Instead, use .onnx models for faster performance due to optimized inference capabilities.

Resources

Project Slide Deck: View on Canva

Dataset Files: Google Drive Link
