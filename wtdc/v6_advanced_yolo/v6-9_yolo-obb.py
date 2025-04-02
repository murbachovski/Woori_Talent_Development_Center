from ultralytics import YOLO
import cv2

# 모델 로드
# model = YOLO('yolo11n.pt')
model = YOLO('yolo11n-obb.pt')

# 모델 예측
results = model(
    "https://ultralytics.com/images/boats.jpg"
)

# 결과 저장
image = results[0].plot()
cv2.imwrite("result_obb.jpg", image)

# https://docs.ultralytics.com/ko/tasks/obb/


# ERROR
# https://ultralytics.com/images/boats.jpg locally at boats.jpg
# WARNING ⚠️ Image Read Error C:\Users\Administrator\Desktop\ai\boats.jpg
# Backend tkagg is interactive backend. Turning interactive mode on.
# ValueError: need at least one array to stack