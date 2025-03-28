# from ultralytics import YOLO

# # Load a model
# model = YOLO("yolo11n-pose.pt")  # load a pretrained model (recommended for training)

# # Train the model
# results = model.train(data="hand-keypoints.yaml", epochs=100, imgsz=640)


from ultralytics.solutions.parking_management import ParkingPtsSelection

parking_selector = ParkingPtsSelection()

# import cv2

# from ultralytics import solutions

# # Video capture
# cap = cv2.VideoCapture("wtdc/parking.mp4")
# assert cap.isOpened(), "Error reading video file"

# # Video writer
# # w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))
# # video_writer = cv2.VideoWriter("parking management.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

# # Initialize parking management object
# parkingmanager = solutions.ParkingManagement(
#     model="yolo11n.pt",  # path to model file
#     json_file="wtdc/v6_advanced_yolo/bounding_boxes.json",  # path to parking annotations file
#     show=True
# )

# while cap.isOpened():
#     ret, im0 = cap.read()
#     if not ret:
#         break

#     results = parkingmanager(im0)

#     # print(results)  # access the output

#     # video_writer.write(results.plot_im)  # write the processed frame.

# cap.release()
# # video_writer.release()
# cv2.destroyAllWindows()  # destroy all opened windows