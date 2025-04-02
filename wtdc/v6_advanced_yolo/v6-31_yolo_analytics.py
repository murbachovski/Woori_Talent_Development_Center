from ultralytics import solutions
import cv2

cap = cv2.VideoCapture(0)

analytics = solutions.Analytics(
    # model="yolo11n.pt",
    show=True,
    analytics_type="pie"
)

frame_count = 0
while cap.isOpened():
    success, frame = cap.read()
        
    if success:
        frame_count += 1
        results = analytics(frame, frame_count)
    else:
        break
    
cap.release()
cv2.destroyAllWindows()
