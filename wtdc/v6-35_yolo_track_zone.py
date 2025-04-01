from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("heatmap.mp4")

# 비디오 정보 가져오기
w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = int(cap.get(cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter(
    "trackzone.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (w, h)
)

# 구역 설정
region_points = [(13, 395), (16, 1024), (944, 1011)]
# Clicked : 13, 395
# Clicked : 16, 1024
# Clicked : 944, 1011
# Clicked : 918, 323

# TrackZone 객체 생성
trackzone = solutions.TrackZone(
    model="yolo11n.pt",
    region=region_points,
    show=False,
    classes=[0]
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    
    results = trackzone(frame)
    video_writer.write(results.plot_im)
    
cap.release()
video_writer.release()
cv2.destroyAllWindows()