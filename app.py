from flask import Flask, render_template, request, send_file, jsonify
import os
import torch
from PIL import Image
import cv2
import uuid

app = Flask(__name__)

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s')  # Load a pretrained model (recommended for testing)

# Set upload and result folder
UPLOAD_FOLDER = 'static/uploads/'
RESULT_FOLDER = 'static/results/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['RESULT_FOLDER'] = RESULT_FOLDER

# Ensure the upload and result folders exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(RESULT_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        return jsonify({"error": "No file uploaded"}), 400
    
    file = request.files['file']
    
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400
    
    if file:
        # Save the uploaded image
        original_filename = file.filename
        file_name = str(uuid.uuid4()) + os.path.splitext(original_filename)[1]
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file_name)
        file.save(file_path)

        # Run YOLOv5 model on the uploaded image
        results = model(file_path)
        
        # Save the results with bounding boxes
        result_filename = f"{os.path.splitext(file_name)[0]}_result.jpg"
        result_path = os.path.join(app.config['RESULT_FOLDER'], result_filename)
        results.save(save_dir=app.config['RESULT_FOLDER'], exist_ok=True)
        
        # Rename the result file to match our expected format
        os.rename(os.path.join(app.config['RESULT_FOLDER'], file_name), result_path)

        return jsonify({"result": f"/static/results/{result_filename}"})

if __name__ == "__main__":
    app.run(debug=True)
