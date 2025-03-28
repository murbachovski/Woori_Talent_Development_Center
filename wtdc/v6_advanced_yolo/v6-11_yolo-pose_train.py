from ultralytics import YOLO

# 모델 로드
model = YOLO("yolo11n-pose.pt")

# 모델 훈련
results = model.train(
    data="hand-keypoints.yaml",
    epochs=1000,
    imgsz=640
)

# 학습 완료해서 예측까지 된 사람은
# epochs, imgsz, batch 변경해보기!!
# Train할때 데이터 imgsz=320 => Predict imgsz=320
