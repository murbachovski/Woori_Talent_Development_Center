from ultralytics import solutions
import cv2

# cap = cv2.VideoCapture("heatmap.mp4")
cap = cv2.VideoCapture(0)

isegment = solutions.InstanceSegmentation(
    model="yolo11n-seg.pt",
    show=True,
    # track_ids=0
)

while cap.isOpened():
    success, frame = cap.read()
    
    if not success:
        break
    
    results = isegment(frame)
    print(f"results : {results}")
    print(f"isegment.track_ids: {isegment.track_ids}")  
    
cap.release()
cv2.destroyAllWindows()