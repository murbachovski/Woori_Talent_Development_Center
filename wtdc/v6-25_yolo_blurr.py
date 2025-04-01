from ultralytics import solutions
import cv2

# 비디오 경로 설정
# cap = cv2.VideoCapture("원하시는 영상 경로")
cap = cv2.VideoCapture("wtdc/v6_advanced_yolo/vehicles.mp4")

# blurr 객체 생성
blurrer = solutions.ObjectBlurrer(
    model="yolo11n.pt",
    show=True,
    blur_ratio=0.1
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success: # => 프레임을 읽지 못하거나 끝났을때 처리
        break
    
    re_frame = cv2.resize(frame, (640, 480))
    results = blurrer(re_frame)
    
cap.release()
cv2.destroyAllWindows()