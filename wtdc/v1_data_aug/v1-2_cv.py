import cv2
import matplotlib.pyplot as plt

# 이미지 로드 
img = cv2.imread('wtdc\_data\data.PNG')

# BGR => RGB 변환(OpenCV는 기본적으로 BGR 형식을 사용)
# img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
a = cv2.resize(img, (50,50))
a.show()

# 이미지 반전
img_flipped = cv2.flip(img, 1) # 1은 수평 반전, 0은 수직 반전, 둘다는 -1

# 이미지 대비 조정
img_contrast = cv2.convertScaleAbs(img, alpha=2.0)

# 결과 확인
fig, ax = plt.subplots(1, 3, figsize=(15, 10))

# 기본 이미지
ax[0].imshow(img)
ax[0].axis('off')
ax[0].set_title('Orign')

# 반전 이미지
ax[1].imshow(img_flipped)
ax[1].axis('off')
ax[1].set_title('Flip')

# 대비 이미지
ax[2].imshow(img_contrast)
ax[2].axis('off')
ax[2].set_title('Contrast')

plt.show()

# cv2.imwrite("저장할 이미지 파일 이름.jpg", 이미지 파일 변수)
cv2.imwrite("flipped.jpg", img_flipped)