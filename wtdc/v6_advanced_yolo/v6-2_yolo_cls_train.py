from ultralytics import YOLO

# 1. 모델 로드
model = YOLO("yolo11n-cls.pt")

# 2. 모델 훈련
model.train(
    data="wtdc/v6_advanced_yolo/datasets", # 훈련 데이터셋 경로
    epochs=100, # => 학습 횟수는 우선 본인이 원하는 만큼
    # batch=2,
    imgsz=320,
    patience=1
)

# 데이터셋 클래스 3개 이상 학습 후 예측 확인해보기
# 각 클래스 이미지는 10장 이상!!
# datasets/
#           train/
#                   class1/
#                           images...
#                   class2/
#                           images...
#                   class3/
#                           images...
#           val/
#                   class1/
#                           images...
#                   class2/
#                           images...
#                   class3/
#                           images...
#           test/
#                   class1/
#                           images...
#                   class2/
#                           images...
#                   class3/
#                           images...

# 훈련 다 된 사람은 loss, mAP50-95, mAP50 용어 찾아보기!!
# 교재
# 160p ~ 195p => 데이터 관련
# 196p ~ 198p => 데이터 전처리
# 279p ~ 302p => 평가 지표 용어 설명