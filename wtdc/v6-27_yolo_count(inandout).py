from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap =cv2.VideoCapture("wtdc/v6_advanced_yolo/vehicles.mp4")

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter(
    "test.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (w, h)
)

count_points = [(100, 1000), (3000, 1000)] # line
# count_points = [(), (), (), ()] # rectangle
# count_points = [(), (), (), (), (), (), ()] # polygon

# count 객체 생성
counter = solutions.ObjectCounter(
    mode1="yolo11n.pt",
    show=True,
    region=count_points,
    # tracker='botsort.yaml'
    # classes=[]
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    # re_frame = cv2.resize(frame, (640, 480))
    results = counter(frame)
    # re_results = counter(re_frame)
    
    video_writer.write(results.plot_im)
    
cap.release()
video_writer.release()
cv2.destroyAllWindows()