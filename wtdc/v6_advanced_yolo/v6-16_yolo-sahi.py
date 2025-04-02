from sahi.predict import get_sliced_prediction
from sahi import AutoDetectionModel

# 모델 경로 설정
model_path = "yolo11n.pt"

# 모델 예측 준비
detection_model = AutoDetectionModel.from_pretrained(
    model_type="ultralytics",
    model_path=model_path,
    confidence_threshold=0.4 # => 점수, 정확도 
)

# sahi 예측
results = get_sliced_prediction(
    # "wtdc/small-vehicles1.jpeg",
    # "wtdc/sahi-person.jpg",
    "wtdc/distance.mp4",
    detection_model,
    slice_height=500,
    slice_width=500,
    overlap_height_ratio=0.1,
    overlap_width_ratio=0.1
)

# 예측 결과 시각화
results.export_visuals(export_dir="sahi/slice/video")
print("SAHI_SUCCESS")

# sahi from video
# https://ultralytics.medium.com/using-ultralytics-yolov8-with-sahi-on-videos-3d524087dd33