# Project Phát hiện gian lận trên hệ thống Elearning
> Group 01
> Lớp 48K29.2, trường đại học kinh tế Đà Nẵng.
- Sử dụng heroku để xử lí ảnh và mongodb để lưu kết quả.
- Huấn luyện bằng model YOLO 11 của ultralytics:
> Trích xuất tính năng nâng cao: YOLO11 sử dụng kiến trúc xương sống và cổ được cải tiến, giúp tăng cường khả năng trích xuất tính năng để phát hiện đối tượng chính xác hơn và thực hiện tác vụ phức tạp.
> Được tối ưu hóa cho hiệu quả và tốc độ: YOLO11 giới thiệu các thiết kế kiến trúc tinh tế và quy trình đào tạo được tối ưu hóa, mang lại tốc độ xử lý nhanh hơn và duy trì sự cân bằng tối ưu giữa độ chính xác và hiệu suất.
> Độ chính xác cao hơn với ít tham số hơn: Với những tiến bộ trong thiết kế mô hình, YOLO11m đạt được Độ chính xác trung bình (mAP) cao hơn trên tập dữ liệu COCO trong khi sử dụng ít hơn 22% tham số so với YOLOv8m , giúp tính toán hiệu quả mà không ảnh hưởng đến độ chính xác.
> Khả năng thích ứng trong nhiều môi trường: YOLO11 có thể được triển khai liền mạch trên nhiều môi trường khác nhau, bao gồm các thiết bị biên, nền tảng đám mây và hệ thống hỗ trợ NVIDIA GPU đảm bảo tính linh hoạt tối đa.
> Phạm vi rộng các tác vụ được hỗ trợ: Cho dù đó là phát hiện đối tượng, phân đoạn thể hiện, phân loại hình ảnh, ước tính tư thế hay phát hiện đối tượng theo hướng (OBB), YOLO11 được thiết kế để giải quyết nhiều thách thức khác nhau về thị giác máy tính.
- Không vượt giới hạn slug size của heroku (<500mb).
- Nhưng memory của heroku có thể bị quá tải (>1gb).
- Lưu ý: web dyno của heroky sẽ có thể không free, bản free không chạy liên tục 24/7 được.
