# Cheating Detection on E-learning System

## Group 01  
Class 48K29.2, University of Economics, Da Nang

## Project Overview
This project focuses on detecting cheating behaviors in an e-learning environment using YOLO and Heroku for image processing, with MongoDB to store results.

## Technologies Used
- **Heroku**: Handles image processing.
- **MongoDB**: Stores detection results.
- **YOLO 11 (Ultralytics)** for model training:
  - **Advanced feature extraction**: YOLO11 utilizes an improved backbone and neck architecture to enhance object detection accuracy and handle complex tasks.
  - **Optimized for efficiency and speed**: YOLO11 introduces refined architectural designs and optimized training processes, offering faster inference speeds while maintaining an optimal balance between accuracy and performance.
  - **Higher accuracy with fewer parameters**: YOLO11m achieves a higher mean Average Precision (mAP) on the COCO dataset while using **22% fewer parameters** than YOLOv8m, making computations more efficient without sacrificing accuracy.
  - **Adaptability across environments**: YOLO11 can be seamlessly deployed across various environments, including edge devices, cloud platforms, and NVIDIA GPU-supported systems, ensuring maximum flexibility.
  - **Wide range of supported tasks**: YOLO11 is designed for multiple computer vision challenges, including object detection, instance segmentation, image classification, pose estimation, and oriented object detection (OBB).

## Deployment Considerations
### Heroku Constraints
- **Slug size limit (<500MB)**
  - Installing `ultralytics` directly in `requirements.txt` may cause errors.
- **Memory constraints (>1GB)**
  - Requires a **web dyno performance** tier (must have a billing history on Heroku).
  - **Note**: Heroku web dynos are not always free; free plans do not run 24/7.

### Important Notes
- **Private keys in `server.py` should be configured separately on Heroku**.
- **A custom browser instance is required to send requests to the Heroku server for processing and fraud detection**.
- **Use `.onnx` models instead of `.pt` models** for faster inference due to optimized processing.

## Resources
- **Project Slide Deck**: [View on Canva](https://www.canva.com/design/DAGZCwukvYs/hKtLQSynDBiaWM8Xj-Umlg/edit)
- **Dataset Files**: [Google Drive Link](https://drive.google.com/drive/folders/1yMAa2kS8hEY1qugx7as4dGPG1D0FjM3F?fbclid=IwY2xjawIerl1leHRuA2FlbQIxMAABHW9L6700nEN5Esi9TODyXAvM-luxcjDGrG4KSsl9ISXdu87Te4eZRYcNVQ_aem_jwrchz3NcqmGykHgcTlAaw)


