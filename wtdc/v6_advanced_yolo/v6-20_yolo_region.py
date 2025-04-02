from ultralytics import solutions
import cv2

# 이미지 파일 열기
im0 = cv2.imread("wtdc/region1.jpg")
im0 = cv2.resize(im0, (640, 480))

# 좌표 설정
region_points = {
    "region-01" : [(259, 364), (210, 479), (528, 478), (457, 353)],
    "region-02" : [(244, 364), (248, 329), (9, 320), (2, 359)],
    "region-03" : [(492, 317), (635, 313), (551, 262), (446, 268)]
}

# RegionCounter 객체 생성
region = solutions.RegionCounter(
    model='yolo11n.pt',
    show=True,
    region=region_points
)

# Region 계산
results = region(im0)
print(results)

cv2.waitKey(0)