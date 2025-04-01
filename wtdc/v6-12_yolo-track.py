from ultralytics import YOLO
import cv2
import timeit

# 모델 로드
model = YOLO("yolo11n.pt")

# 비디오 생성
cap = cv2.VideoCapture("wtdc/track2.mp4")

# 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if success:
        results = model.track(frame, persist=True, stream=True, imgsz=640)

        for result in results:
            # 시각화
            annotated_frame = result.plot()

            cv2.namedWindow("YOLO_TRACK", cv2.WINDOW_NORMAL)
            cv2.imshow("YOLO_TRACK", annotated_frame)
            
        # q 키 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("종료")
            break
    else:
        print("프레임 확인해주세요.")
        break

cap.release()
cv2.destroyAllWindows()
