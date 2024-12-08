from flask import Flask, request
from flask_cors import CORS
from ultralytics import YOLO
from PIL import Image
import io

app = Flask(__name__)
CORS(app)

# Tải mô hình đã huấn luyện
model = YOLO('best.onnx')

def read_image(file):
    # Đọc ảnh từ file và chuyển đổi sang định dạng mà mô hình YOLO hỗ trợ
    image = Image.open(io.BytesIO(file)).convert('RGB')
    return image

@app.route("/predict", methods=["POST"])
def predict():
    # Nhận ảnh từ POST request
    file = request.files['image'].read()
    
    # Đọc và chuyển đổi ảnh
    image = read_image(file)
    
    # Chạy mô hình nhận diện ảnh
    results = model(image)
    for result in results:
        print(result.boxes)  # Print detection boxes
        #result.show()  # Display the annotated image
        #result.save(filename="result.jpg")  # Save annotated imag
    
    return results[0].to_json()

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)