from ultralytics import YOLO

# 1. YOLO 모델 로드
model = YOLO("yolo11n.pt")

# 2. 모델 예측
results = model("wtdc\_data\input.mp4", save=True)

# https://docs.ultralytics.com