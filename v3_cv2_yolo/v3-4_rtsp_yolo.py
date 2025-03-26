from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv002.stream/playlist.m3u8")
# cap.set(cv2.CAP_PROP_BUFFERSIZE, 2)
# cap.set(cv2.CAP_PROP_FPS, 10)

# 2. 모델 로드
model = YOLO("yolo11n.pt")

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        results = model(frame)
        annotated_frame = results[0].plot()
        cv2.namedWindow("HTTPS", cv2.WINDOW_NORMAL)
        cv2.imshow("HTTPS", annotated_frame)
        
        # "q"키를 눌러서 나가기
        if cv2.waitKey(1) & 0xFF ==ord('q'):
            print("q를 눌러서 종료했습니다.")
            break
        
cap.release()
cv2.destroyAllWindows()