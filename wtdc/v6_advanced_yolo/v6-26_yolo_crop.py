from ultralytics import solutions
import cv2

# 비디오 경로 설정
# cap = cv2.VideoCapture("wtdc/_data/track.mp4")
cap = cv2.VideoCapture("https://cctvsec.ktict.co.kr/6570/slzNyfjZScqUil9yWzqaoSoAXhgnokf15yfXkRLrX/aaedsUQoOYReWU39ySwXTq")

# crop 객체 생성
cropper = solutions.ObjectCropper(
    model="yolo11n.pt",
    show=True,
    conf=0.6,
    classes=[0, 2] # => person, car
    # crop_dir="./cropped"
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    
    # re_frame = cv2.resize(frame, (640, 480))
    results = cropper(frame)
    print(results)
    cv2.waitKey(1)
    
cap.release()
cv2.destroyAllWindows()