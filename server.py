from flask import Flask, request, jsonify
import torch

app = Flask(__name__)

# Tải mô hình đã huấn luyện
model = torch.load('best.pt')

@app.route("/predict", methods=["POST"])
def predict():
    # Nhận ảnh từ POST request
    file = request.files['image']
    img = file.read()
    
    # Chạy mô hình nhận diện ảnh
    results = model(img)

    # Trả về kết quả nhận diện dưới dạng JSON
    return jsonify(results.pandas().xywh)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)