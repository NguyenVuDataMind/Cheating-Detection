from flask import Flask, request, jsonify
from flask_cors import CORS
from ultralytics import YOLO
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Load the trained model
model = YOLO('best.onnx')

def read_image(file):
    # Read the image from file and convert it to a format supported by YOLO model
    image = Image.open(io.BytesIO(file)).convert('RGB')
    return image

@app.route("/predict", methods=["POST"])
def predict():
    # Receive the image from the POST request
    file = request.files['image'].read()
    
    # Read and convert the image
    image = read_image(file)
    
    # Run the model on the image
    results = model(image)
    
    # Extract detection results
    detections = []
    for box in results[0].boxes:
        detection = {
            "class_name": int(box.cls.item()),  # Assuming class names are integers
            "confidence": float(box.conf.item()),
            "x": float(box.xyxy[0][0].item()),
            "y": float(box.xyxy[0][1].item()),
            "width": float(box.xyxy[0][2].item() - box.xyxy[0][0].item()),
            "height": float(box.xyxy[0][3].item() - box.xyxy[0][1].item())
        }
        detections.append(detection)
    
    return jsonify(detections)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
