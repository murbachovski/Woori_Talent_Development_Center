import cv2

cap = cv2.VideoCapture("heatmap.mp4")

success, frame = cap.read()
if success:
    cv2.imwrite("./heatmap.jpg", frame)
    
cap.release()