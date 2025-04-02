from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("heatmap-parking.mp4") 

# Heatmap 설정
heatmap = solutions.Heatmap(
    colormap=cv2.COLORMAP_PARULA,
    model='yolo11n.pt',
    show=True,
    # classes=2,
    conf=0.1
)


# 비디오 실행
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("비디오 프레임을 확인해주세요.")
        break
   
    # 영상 출력이 너무 크다면
    # cv2.resizeWindow("Ultralytics Solutions", 640, 480)
    # cv2.imshow("Ultralytics Solutions", heat_frame) => 배열 오류
    cv2.resize(frame, (640,360)),
    cv2.namedWindow("Ultralytics Solutions", cv2.WINDOW_NORMAL)

    # Heatmap 생성
    heat_frame = heatmap(frame)
    
    # "q" 키를 눌러서 종료
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# 비디오 해제
cap.release()
cv2.destroyAllWindows()