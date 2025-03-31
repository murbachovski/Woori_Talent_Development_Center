from ultralytics import solutions
import cv2

# 비디오 경로 설정
cap = cv2.VideoCapture("wtdc/_data/region.mp4")

# 특정 좌표 설정
region_points = {
    # "region-01" : [(87, 13), (507, 14), (631, 246), (430, 449), (207, 448), (44, 225)]
    "region-01" : [(17, 14), (13, 67), (617, 76), (619, 14)],
    "region-02" : [(22, 148), (18, 204), (603, 220), (606, 145)],
    "region-03" : [(32, 291), (32, 344), (611, 356), (610, 297)],
    "region-04" : [(31, 432), (32, 476), (618, 477), (617, 440)]
}

# 구역 설정
region = solutions.RegionCounter(
    model="yolo11n.pt",
    region=region_points,
    show=True,
    conf=0.2,
)

# 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        break
    
    region1 = region.region_counts.get(("region-01"), 0)
    region2 = region.region_counts.get(("region-02"), 0)
    region3 = region.region_counts.get(("region-03"), 0)
    region4 = region.region_counts.get(("region-04"), 0)
    print(f"region1: {region1}, region2: {region2}, region3: {region3}, region4: {region4}")
    
    re_frame = cv2.resize(frame, (640, 480))
    cv2.namedWindow("Ultralytics Solutions", cv2.WINDOW_NORMAL)
    
    cv2.putText(
        re_frame, # (나타낼 화면)
        f"region1: {region1}, region2: {region2}, region3: {region3}, region4: {region4}", # (텍스트)
        (10, 30), # (표시 위치)
        cv2.FONT_HERSHEY_SIMPLEX, # (폰트)
        0.7, # (텍스트 굵기)
        (0, 255, 0), # (텍스트 색상)
        1, # (???)
        cv2.LINE_AA # (???)
    )   
    
    # 특정 구역 계산
    im0 = region(re_frame)
    # print(im0)
    
# 비디오 해제
cap.release()
cv2.destroyAllWindows()

# 1. 터미널에 구역 탐지 객체 수 출력
# 2. 영상 화면에 구역 탐지 객체 수 출력 => 17:20분 까지 진행
