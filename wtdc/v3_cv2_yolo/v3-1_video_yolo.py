from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/_data/input.mp4")

# 2. 카메라 해상도 설정
# cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
# cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
# org_w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# org_h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # 버퍼 크기 줄이기

fps = cap.get(cv2.CAP_PROP_FPS)

# 3. 모델 로드
model = YOLO("yolo11n.pt")

# 4. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        
        # annotated_frame = cv2.resize(annotated_frame, (org_w, org_h))
        
        print(f"FPS : {fps}")
        cv2.namedWindow("VIDEO", cv2.WINDOW_NORMAL)
        cv2.imshow("VIDEO", annotated_frame)
        # "q" 키를 눌러서 종료
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
        
cap.release()
cv2.destroyAllWindows()

# pip install opencv-contrib-python