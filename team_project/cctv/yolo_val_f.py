from ultralytics import YOLO
import os
from pathlib import Path

# 모델 불러오기 (경로에 맞게 yolov11n.pt로 변경 가능)
model = YOLO("C:/Users/Administrator/Desktop/ai/runs/detect/train/weights/best.pt")

# 이미지 폴더 경로
image_folder = "C:/Users/Administrator/Desktop/ai/team_project/cctv/datasets/coco8/images/test"

# 결과 저장 폴더
output_folder = "team_project/test/"
os.makedirs(output_folder, exist_ok=True)

# 폴더 내 모든 이미지 예측
image_extensions = ['.jpg', '.jpeg', '.png', '.bmp']
image_paths = [str(p) for p in Path(image_folder).glob("*") if p.suffix.lower() in image_extensions]

for img_path in image_paths:
    results = model(img_path, save=True, save_txt=True, project=output_folder, name='results')

print("예측 완료!")
