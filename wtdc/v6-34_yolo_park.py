from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/v6_advanced_yolo/parking2.mp4")

# 비디오 정보 가져오기
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
# w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
# h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
# fps = int(cap.get(cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter(
    "park_result.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (w, h)
)

# parking 객체 생성
parkingmanager = solutions.ParkingManagement(
    model="yolo11x.pt",
    show=True,
    json_file="bounding_boxes_2.json"
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    
    results = parkingmanager(frame)
    video_writer.write(results.plot_im)
    
# 비디오 해제
cap.release()
video_writer.release()
cv2.destroyAllWindows()

# 오탐 => 모델 훈련 데이터셋은 640 이미지인데 영상이 너무 큰 해상도
# 해결방안 => 영상에서 이미지 저장할때 640 이미지로 저장 => 640 이미지로 json 파일 출력 => 추론 및 비디오 저장