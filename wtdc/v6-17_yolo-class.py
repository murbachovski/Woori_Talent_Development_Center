from ultralytics import YOLO

# 1. 모델 로드
model = YOLO('yolo11n.pt')

# 2. 모델 예측
results = model(
    # "wtdc/test-class.jpeg",
    "wtdc/_data/test-class.jpg",
    save=True,
    # classes=60 # => 단일 객체
    classes=[41, 60] # => 복수 객체
)

# dining table class만 탐지되도록 수정해주세요.
# 단일, 복수 객체 탐지 진행해보기
# 1개, 2개, 3개 원하는 객체 탐지 진행