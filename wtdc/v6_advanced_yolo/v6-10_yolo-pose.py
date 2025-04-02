from ultralytics import YOLO
import cv2

# 모델 로드
model = YOLO("runs/pose/train8/weights/best.pt")

# 비디오 가져오기
# cap = cv2.VideoCapture("wtdc/_data/pose.mp4")
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("카메라 연결 확인해주세요.")
    exit()
    
while True:
    success, frame = cap.read()
    if not success:
        print("프레임 확인해주세요.")
        break
    
    # YOLO모델 예측
    results = model(frame, imgsz=320, conf=0.7)
    
    # 결과 시각화
    annotated_frame = results[0].plot()
    
    # 키포인트 좌표 값 출력
    # print(dir(results[0]))
    print(results[0].keypoints.xy)
    
    # 영상 출력
    cv2.namedWindow("YOLO_POSE", cv2.WINDOW_NORMAL) # => 영상 화면 크게 출력 방지
    cv2.imshow("YOLO_POSE", annotated_frame)
    
    # q 키를 눌러서 나가기
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
# 리소스 해제
cap.release()
cv2.destroyAllWindows()

# https://docs.ultralytics.com/tasks/pose/ 
# 1. pose 모델 학습하기 위한 데이터셋 구축 방법
# 2. 키포인트 개수와 클래스 정리
# 3. 모델 추론 후 키포인트 좌표 값 출력시키기 => dir() 로 찾아보기