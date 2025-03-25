import albumentations as A
import cv2
import matplotlib.pyplot as plt

# 이미지 로드
img = cv2.imread("wtdc/_data/data.PNG")

# BGR2RGB
img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

# Albumentations 설정
transform = A.Compose([
    # 회전
    A.Rotate(limit=20, p=1.0),
    # 밝기
    A.RandomBrightnessContrast(p=1.0)    
])

# 이미지 변환
augmented = transform(image=img)
img_augmented = augmented['image']

# 결과 확인
plt.imshow(img_augmented)
plt.axis('off')
plt.title("Augmented Image")
plt.show()