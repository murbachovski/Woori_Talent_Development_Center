from ultralytics import solutions
import cv2

cap = cv2.VideoCapture("wtdc/v6_advanced_yolo/vehicles.mp4")
cap.set(cv2.CAP_PROP_FPS, 200)

w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

video_writer = cv2.VideoWriter(
    "speed_test.avi",
    cv2.VideoWriter_fourcc(*"MJPG"),
    fps,
    (w, h)
)

# speed_region = [(160, 235), (467, 256)] => 640, 4870
# speed_region = [(99, 377), (1228, 376)] # => 1280, 680
speed_region = [(100, 1000), (3000, 1000)] # line

speed_estimator = solutions.SpeedEstimator(
    model="yolov5s.pt",
    show=True,
    region=speed_region,
    line_width=1
)

while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        print("프레임을 읽지 못했거나 영상 재생이 완료됨")
        break
    # re_frame = cv2.resize(frame, (1280, 680))
    
    results = speed_estimator(frame)
    print(results)
    video_writer.write(results.plot_im)
    
cap.release()
video_writer.release()
cv2.destroyAllWindows()
  