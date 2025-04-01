from ultralytics import YOLO
import cv2

# 1. 모델 로드
model = YOLO("runs/classify/train/weights/best.pt")

# 2. 모델 예측
results = model(
    "wtdc/v6_advanced_yolo/datasets/test/rock/8.jpg",
    save=True,
)

# 3. 이미지 저장
# image = results[0].plot()
# cv2.imwrite("results_image_cls.jpg", image)