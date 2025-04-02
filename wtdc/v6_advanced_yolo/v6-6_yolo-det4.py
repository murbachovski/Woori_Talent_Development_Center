from ultralytics import YOLO

# 1. 모델 로드
model = YOLO('yolo11n.pt')

# 2. 모델 예측
results = model(
    "wtdc\_data\car.PNG",
    max_det=10, # 최대 감지 개수 설정
    conf=0.5, # 임계치 설정
    save_txt=True, # 텍스트로 결과 정보 저장 여부
    save_conf=True, # 탐지 신뢰도 값 저장 여부
    save_crop=True, # 탐지된 객체 이미지 저장 여부
    save=True,
    visualize=True
)

# https://docs.ultralytics.com/ko/modes/predict/#working-with-results