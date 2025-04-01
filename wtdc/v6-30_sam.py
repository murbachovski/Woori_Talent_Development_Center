from ultralytics import SAM

# 모델 로드
model = SAM("sam_b.pt")

# 모델 추론
model("wtdc/_data/test-class.jpg", save=True)