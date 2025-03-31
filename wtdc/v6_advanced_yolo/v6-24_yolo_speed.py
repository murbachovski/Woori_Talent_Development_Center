from ultralytics import solutions
import cv2

cap = cv2.VideoCapture("wtdc/v6_advanced_yolo/vehicles.mp4")
cap.set(cv2.CAP_PROP_FPS, 200)

# speed_region = [(160, 235), (467, 256)] => 640, 4870
speed_region = [(99, 377), (1228, 376)] # => 1280, 680

speed_estimator = solutions.SpeedEstimator(
    model="yolov5s.pt",
    show=True,
    region=speed_region,
    line_width=3
)

while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("프레임을 읽지 못했거나 영상 재생이 완료됨")
        break
    re_frame = cv2.resize(frame, (1280, 680))
    
    results = speed_estimator(re_frame)
    print(results)
    
cap.release()
cv2.destroyAllWindows()
  