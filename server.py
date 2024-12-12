from flask import Flask, request, jsonify
from PIL import Image
import io
import json
import base64
import numpy as np
from ultralytics import YOLO
from pymongo import MongoClient
from flask_cors import CORS
import cv2
import gc

app = Flask(__name__)

cors = CORS(app, resources={r"/*": {"origins": "https://yumyum.social"}})

# Load the trained model
model = YOLO('best.onnx')

client = MongoClient('mongodb+srv://MLadmin:admin1021@machinelearning.so3qxxp.mongodb.net/')
db = client['MACHINELEARNING']

def read_image(file):
    image = Image.open(io.BytesIO(file)).convert('RGB')
    return image

def non_max_suppression(boxes, iou_threshold):
    if len(boxes) == 0:
        return []

    # Convert to numpy array for easier manipulation
    boxes = np.array(boxes)

    # Extract coordinates and confidence scores
    x1 = boxes[:, 0]
    y1 = boxes[:, 1]
    x2 = boxes[:, 2]
    y2 = boxes[:, 3]
    scores = boxes[:, 4]

    # Compute the area of the bounding boxes
    areas = (x2 - x1 + 1) * (y2 - y1 + 1)

    # Sort the bounding boxes by the confidence scores in descending order
    order = scores.argsort()[::-1]

    keep = []
    while order.size > 0:
        i = order[0]
        keep.append(i)

        xx1 = np.maximum(x1[i], x1[order[1:]])
        yy1 = np.maximum(y1[i], y1[order[1:]])
        xx2 = np.minimum(x2[i], x2[order[1:]])
        yy2 = np.minimum(y2[i], y2[order[1:]])

        w = np.maximum(0, xx2 - xx1 + 1)
        h = np.maximum(0, yy2 - yy1 + 1)

        inter = w * h
        iou = inter / (areas[i] + areas[order[1:]] - inter)

        inds = np.where(iou <= iou_threshold)[0]
        order = order[inds + 1]

    return boxes[keep].tolist()

@app.route("/predict", methods=["POST"])
def predict():
    # Extract user ID and other information from the request
    quiz_id = request.form.get('quiz_id')
    user_id = request.form.get('user_id')
    device_info = request.form.get('device_info')
    date_time = request.form.get('date_time')
    
    # Set the collection name dynamically based on user ID and device info
    collection_name = f"{quiz_id}"
    collection = db[collection_name]
    
    # Receive the image from the POST request
    file = request.files['image'].read()
    
    # Read and convert the image
    image = read_image(file)
    
    # Run the model on the image
    results = model(image)
    
    # Resize the image to a width of 1024 while maintaining the aspect ratio
    image_np = np.array(image)
    new_width = 1024
    new_height = int(image_np.shape[0] * (new_width / image_np.shape[1]))
    resized_image = cv2.resize(image_np, (new_width, new_height))

    # Calculate the scaling factors
    scale_x = new_width / image_np.shape[1]
    scale_y = new_height / image_np.shape[0]

    # Adjust the bounding box coordinates based on the new image dimensions
    adjusted_boxes = []
    for box in results[0].boxes.data.cpu().numpy():
        x1, y1, x2, y2, conf, cls = box
        x1 *= scale_x
        y1 *= scale_y
        x2 *= scale_x
        y2 *= scale_y
        adjusted_boxes.append([float(x1), float(y1), float(x2), float(y2), float(conf), int(cls)])

    # Encode the resized image as a base64 string
    _, buffer = cv2.imencode('.png', resized_image)
    image_base64 = base64.b64encode(buffer).decode('utf-8')
    del buffer
    
    # Apply Non-Maximum Suppression
    iou_threshold = 0.5  # You can adjust this threshold
    nms_boxes = non_max_suppression(adjusted_boxes, iou_threshold)
    del adjusted_boxes
    
    if len(nms_boxes) > 0:
        final_box = nms_boxes[0]
        final_label = results[0].names[int(final_box[5])]
        final_conf = final_box[4]
    else:
        final_box = None
        final_label = None
        final_conf = None
    del nms_boxes
    # Create result_data with only the highest confidence box
    result_data = {
        'masv': user_id,
        'device_info': device_info,
        'date_time': date_time,
        'boxes': [final_box],
        'labels': [final_label],
        'confidences': [final_conf],
        'orig_shape': results[0].orig_shape,
        'image_base64': image_base64
    }
    
    # Check for existing documents with the same masv
    existing_document = collection.find_one({'masv': user_id})

    # Determine if the new document should be inserted
    
    if existing_document:
        should_insert = False
        if 'gian lan' in existing_document['labels'] and 'gian lan' in result_data['labels']:
            existing_confidence = max(existing_document['confidences'])
            new_confidence = max(result_data['confidences'])
            if new_confidence > existing_confidence:
                should_insert = True
            else:
                should_insert = False
        elif 'binh thuong' in existing_document['labels'] and 'gian lan' in result_data['labels']:
            should_insert = True
        # Update the document
        if should_insert:
            collection.replace_one({'masv': user_id}, result_data, upsert=True)
    else:
        should_insert = True
        # Insert the new document
        if should_insert:
            collection.insert_one(result_data)

    del file                # 🟢
    del image               # 🟢
    del resized_image       # 🟢
    del result_data         # 🟢
    del results             # 🟢
    del existing_document   # 🟢
    del image_np            # 🟢
    
    # Extract detection results for response
    detections = []
    
    # Create the detection dictionary for the box with the highest confidence
    detection = {
        "class_name": final_box[5],  # Assuming class names are integers
        "confidence": final_box[4],
        "x": final_box[0],
        "y": final_box[1],
        "width": final_box[2] - final_box[0],
        "height": final_box[3] - final_box[1]
    }

    detections = [detection]
    
    return jsonify({"detections": detections})

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
