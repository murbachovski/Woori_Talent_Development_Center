from ultralytics import YOLO
import os
import torch
print(torch.cuda.is_available())


# Load a model
model = YOLO("runs/detect/train/weights/last.pt")  # load a pretrained model (recommended for training)

# 여러 데이터셋 폴더를 지정
datasets_root_list = [
    "team_project/cctv/datasets/coco8/images",
    "team_project/cctv/datasets/coco8/labels"  # 예시로 추가
]

# 하위 폴더 이름
sub_folders = ["train", "val", "test"]

# 각 데이터셋 폴더마다 개수 출력
for dataset_path in datasets_root_list:
    print(f"\n📁 데이터셋 경로: {dataset_path}")
    for folder in sub_folders:
        folder_path = os.path.join(dataset_path, folder)
        if os.path.exists(folder_path):
            file_count = len([f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f))])
            print(f" - {folder} 폴더 : {file_count}개 파일")
        else:
            print(f" - {folder} 폴더가 존재하지 않습니다.")

# Train the model
results = model.train(data="team_project/cctv/datasets/coco8.yaml",
                      epochs=500,
                      imgsz=640,
                    #   resume=True,
                      patience=10,
                      # 25.04.08.추가
                      cache=True, # 메모리 정리
                      batch=64,
                      freeze=10
                    #   visualize=True, # 학습 중 모델이 어떻게 예측하는지 이미지로 시각화
                    #   device=0
                      )


# tensorboard --logdir="C:/Users/Administrator/Desktop/ai/runs/detect/train"