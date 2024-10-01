# YOLOv5 Object Detection Web App

This project is a web-based application that allows users to upload an image and run object detection using a YOLOv5 model trained on the COCO2017 dataset. The app is built with **Flask** for the backend and uses **YOLOv5** for detecting objects in the input images. Detected objects are highlighted with bounding boxes, and the processed image is displayed to the user.

## Features

- Upload an image via the web interface.
- Detects objects using YOLOv5 with COCO2017-trained weights.
- Displays the output image with bounding boxes for detected objects.
- Easy to deploy and use.

## Demo

You can run the app locally on your PC. Just follow these steps:

1. Clone the repository:
   ```bash
   git clone https://github.com/PranitThombare/Object_detection_application.git
   cd Object_detection_application

2. Run the Command in Terminal:
   ```bash
   python app.py

## Requirements

Make sure you have the following installed:

- Python 3.7+
- Flask
- PyTorch
- YOLOv5 (installed via PyTorch Hub)
- OpenCV
- PIL (Python Imaging Library)

### Python Libraries:

```bash
Flask==2.1.1
torch==1.9.0
torchvision==0.10.0
opencv-python==4.5.3.56
Pillow==8.2.0
