from ultralytics import YOLO
import time
import cv2

# YOLO 모델 버전 속도, 정확도 비교
# n => s => m => l => x
# nano => smal => medium => large => xlarge

# 1. 모델 목록
models = [
    "yolo11n.pt",
    "yolo11s.pt",
    "yolo11m.pt",
    "yolo11l.pt",
    "yolo11x.pt",
]

# 2. 테스트 이미지
image_path = "wtdc/_data/input.jpg"

# 3. 각 모델에 대해 추론 속도 및 정확도 비교

for i in models:
    # 3-1. 모델 로드
    model = YOLO(i)
    # model = YOLO("yolo11n.pt")

    # 3-2. 모델 추론 시작 시간
    start_time = time.time()

    # 3-3. 이미지에 대한 예측 수행
    results = model(image_path, save=True)

    # 3-4. 모델 추론 종료 시간
    end_time = time.time()

    # 3-5. 모델 추론 시간 계산
    inference_time = end_time - start_time

    # 3-6. 결과 이미지 저장
    image = results[0].plot()
    result_image_path = f"./result_{i.split('.')[0]}.jpg"
    cv2.imwrite(result_image_path, image)
    
    # 3-6. 모델 추론 정보 출력
    print("-----")
    print(f"모델 : {i}")
    print(f"추론 시간: {inference_time}")
    print("-----")

# m, l, x 모델도 비교해주세요.