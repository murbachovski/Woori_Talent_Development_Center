from PIL import Image, ImageEnhance
import matplotlib.pyplot as plt
import cv2

# 이미지 로드
img = Image.open("wtdc\_data\data.PNG")
a = img.transpose(Image.FLIP_TOP_BOTTOM)
a.show()

# 이미지 회전
img_rotated = img.rotate(90)

# 이미지 밝기 조정
enhancer = ImageEnhance.Brightness(img) 
img_brightened = enhancer.enhance(2.0)

# 결과 확인
fig, ax = plt.subplots(1, 3, figsize=(10, 5))

ax[0].imshow(img)
ax[0].axis('off')
ax[0].set_title("ORG_IMAGE")

ax[1].imshow(img_rotated)
ax[1].axis('off')
ax[1].set_title("ROTATED_IMAGE")

ax[2].imshow(img_brightened)
ax[2].axis('off')
ax[2].set_title("BRIGHT")

img_brightened.save("./results.png")

plt.show()

# 이미지 2개 더 튜닝하여 시각화

# img.transpose(Image.FLIP_....)
# a = img.transpose(Image.Transpose.TRANSVERSE)

# a.save('./tmp.png')