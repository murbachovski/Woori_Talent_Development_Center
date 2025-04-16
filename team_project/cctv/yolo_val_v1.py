from ultralytics import YOLO

# Load a model
model = YOLO("C:/Users/Administrator/Desktop/ai/runs/detect/train/weights/best.pt")

# Save validation results to JSON
metrics = model.val(save_json=True)