from ultralytics import YOLO

# 1. 모델 로드
model = YOLO('yolo11n.pt')

# 2. 모델 예측
results = model(
    "wtdc/test-class.jpg",
    save=True
)

# dining table class만 탐지되도록 수정해주세요.