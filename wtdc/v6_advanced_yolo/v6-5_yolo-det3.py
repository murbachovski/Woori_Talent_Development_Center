from ultralytics import YOLO
import cv2

# 1. 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv014.stream/playlist.m3u8")

# 2. 모델 로드
model = YOLO('yolo11n.pt')

# 3. 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        results = model(frame, conf=0.6)
        
        # 4. 상태 정의
        number = len(results[0])
        if number <= 2:
            status = "Normal"
            color = (0, 255, 0) # 초록색
        elif 3 <= number <= 6:
            status = "Warning"
            color = (0, 165, 255) # 주황색
        else:
            status = "Danger"
            color = (0, 0, 255) # 빨간색
            
        print(f"탐지된 개수 : {number}, 상태는 {status} 입니다.")
        
        annotated_frame = results[0].plot()
        
        # 상태 텍스트 추가
        cv2.putText(
            annotated_frame,
            f"Detected : {number}, Status : {status}",
            (10, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2,
            cv2.LINE_AA
        )
        
        # 결과 화면 출력
        cv2.imshow("YOLO", annotated_frame)
        
        # "q"키를 눌러서 나가기
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print("나가기~")
            break
        
# 프로그램 종료
cap.release()
cv2.destroyAllWindows()