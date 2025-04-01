from ultralytics import solutions
import cv2
import threading

# solutions에 있는 기능 두 가지 이상 조합하여 멀티 스레드로 구현
# 예) 같은 영상을 추론 => Car : Crop || Person : blurr
# 12시까지

import cv2
import threading
from ultralytics import solutions

# 비디오 경로 설정
video_crop = "wtdc/_data/track.mp4"
video_blur = "wtdc/v6_advanced_yolo/vehicles.mp4"

# cropper 객체 생성
cropper = solutions.ObjectCropper(
    model="yolo11n.pt",
    show=True,
    conf=0.6,
    classes=[0, 2]  # person, car
)

# blurrer 객체 생성
blurrer = solutions.ObjectBlurrer(
    model="yolo11n.pt",
    show=True,
    blur_ratio=0.1
)

# 객체 자르기 실행 함수
def run_cropper(filename):
    cap = cv2.VideoCapture(filename)
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        results = cropper(frame)
        print("Cropper Results:", results)
        cv2.waitKey(1)
    
    cap.release()
    cv2.destroyAllWindows()

# 객체 블러 처리 실행 함수
def run_blurrer(filename):
    cap = cv2.VideoCapture(filename)
    
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        results = blurrer(frame)
        print("Blurrer Processed Frame")
        cv2.waitKey(1)
    
    cap.release()
    cv2.destroyAllWindows()

# 멀티 스레드 실행
thread_crop = threading.Thread(target=run_cropper, args=(video_crop), daemon=True)
thread_blur = threading.Thread(target=run_blurrer, args=(video_blur), daemon=True)

# 스레드 시작
thread_crop.start()
thread_blur.start()

# 스레드 종료 대기
thread_crop.join()
thread_blur.join()
