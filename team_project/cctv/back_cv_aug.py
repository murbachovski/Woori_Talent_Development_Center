import cv2
import numpy as np
import os
import random

# 이미지 불러오기
image_path = 'team_project/datasets/background2/background_2_000.png'  # 원본 이미지 경로
img = cv2.imread(image_path)

# 출력 폴더 생성
output_dir = 'datasets5'
os.makedirs(output_dir, exist_ok=True)

def change_brightness(img, value):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hsv = hsv.astype(np.int32)  # 먼저 int로 변환
    hsv[..., 2] = np.clip(hsv[..., 2] + value, 0, 255)
    hsv = hsv.astype(np.uint8)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def change_contrast(img, alpha):
    return cv2.convertScaleAbs(img, alpha=alpha, beta=0)

def change_saturation(img, scale):
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV).astype(np.float32)
    hsv[..., 1] *= scale
    hsv[..., 1] = np.clip(hsv[..., 1], 0, 255)
    return cv2.cvtColor(hsv.astype(np.uint8), cv2.COLOR_HSV2BGR)

def add_gaussian_noise(img):
    row, col, ch = img.shape
    mean = 0
    sigma = random.uniform(5, 25)
    gauss = np.random.normal(mean, sigma, (row, col, ch)).reshape(row, col, ch)
    noisy = img + gauss
    return np.clip(noisy, 0, 255).astype(np.uint8)

def apply_blur(img, k=5):
    return cv2.GaussianBlur(img, (k, k), 0)

def add_black_box(img):
    h, w = img.shape[:2]
    box_size = random.randint(20, 100)
    x = random.randint(0, w - box_size)
    y = random.randint(0, h - box_size)
    img_copy = img.copy()
    cv2.rectangle(img_copy, (x, y), (x + box_size, y + box_size), (0, 0, 0), -1)
    return img_copy

def change_color_space(img, mode):
    if mode == 'gray':
        return cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    elif mode == 'lab':
        return cv2.cvtColor(img, cv2.COLOR_BGR2Lab)
    elif mode == 'hsv':
        return cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    return img

# 데이터 생성
for i in range(50):
    aug = img.copy()

    # 랜덤한 조합으로 전처리 수행
    if random.random() < 0.5:
        aug = change_brightness(aug, random.randint(-60, 60))
    if random.random() < 0.5:
        aug = change_contrast(aug, random.uniform(0.5, 2.0))
    if random.random() < 0.5:
        aug = change_saturation(aug, random.uniform(0.5, 1.5))
    if random.random() < 0.3:
        aug = add_gaussian_noise(aug)
    if random.random() < 0.3:
        aug = apply_blur(aug, random.choice([3, 5, 7]))
    if random.random() < 0.3:
        aug = add_black_box(aug)
    if random.random() < 0.2:
        space = random.choice(['gray', 'lab', 'hsv'])
        aug = change_color_space(aug, space)

        # 만약 흑백으로 바뀐 경우 3채널로 복원 (저장 시 BGR 필요)
        if len(aug.shape) == 2:
            aug = cv2.cvtColor(aug, cv2.COLOR_GRAY2BGR)

    # 저장
    save_path = os.path.join(output_dir, f"aug_{i:03d}.jpg")
    cv2.imwrite(save_path, aug)

print("전처리 이미지 생성 완료!")