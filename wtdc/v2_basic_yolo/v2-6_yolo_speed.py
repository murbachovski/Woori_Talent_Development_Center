from ultralytics import YOLO
import cv2
import time

# YOLO 5 ~ 11 모델 속도와 정확도 비교해보세요. (버전 7 제외)
# https://docs.ultralytics.com/models/

# 1. 비교할 YOLO 모델 목록 정의
model_paths = [
    "yolov5n.pt",
    "yolov8n.pt",
    "yolov9t.pt",
    "yolov10n.pt",
    "yolo11n.pt"
]

# 2. 테스트 입력 이미지 경로
image_path = "wtdc/_data/data.PNG"

# 3. 각 모델에 대한 추론 속도 및 결과 비교
for i in model_paths:
    # 3-1. 모델 로드
    model = YOLO(i)
    
    # 3-2. 모델 추론 시작 시간
    start_time = time.time()
    
    # 3-3. 모델 추론
    results = model(image_path, save=True)
    
    # 3-4. 모델 추론 종료 시간
    end_time = time.time()
    
    # 3-5. 모델 추론 시간 계산
    inference_time = end_time - start_time
    
    # 3-6. 모델 추론 결과 시각화
    image = results[0].plot()
    
    # 3-7. 결과 이미지 저장
    result_image_path = f"./result_{i.split('.')[0]}.jpg"
    cv2.imwrite(result_image_path, image)
    
    # 3-8. 모델 정보 출력
    print("-----")
    print(f"모델 : {i}")
    print(f"추론 시간 : {inference_time}")
    print("-----")
    
# 5 Speed: 5.2ms preprocess, 118.8ms inference, 2.7ms postprocess per image at shape (1, 3, 480, 640)
# 8 Speed: 4.0ms preprocess, 98.6ms inference, 1.2ms postprocess per image at shape (1, 3, 480, 640)
# 9 Speed: 4.8ms preprocess, 155.2ms inference, 1.2ms postprocess per image at shape (1, 3, 480, 640)
# 10 Speed: 4.2ms preprocess, 150.5ms inference, 0.5ms postprocess per image at shape (1, 3, 480, 640)
# 11 Speed: 4.2ms preprocess, 100.5ms inference, 1.5ms postprocess per image at shape (1, 3, 480, 640)