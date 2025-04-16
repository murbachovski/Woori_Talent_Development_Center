import requests
import urllib
import json
import pandas as pd
import cv2
import os
import time
from datetime import datetime

#### 요청변수 확인 ####
# 인증키
key = "db5c00dc1fce45c49049bff225a0fea6"

# 도로 유형(ex: 고속도로 / its: 국도)
Type = "its"

# CCTV 유형(1: 실시간 스트리밍 / 2: 동영상 파일 3: 정지 영상)
cctvType = "1"

# 최소 경도 영역
minX = float(120.95)

# 최대 경도 영역
maxX = float(127.02)

# 최소 위도 영역
minY = float(30.55)

# 최대 위도 영역
maxY = float(37.60)

# 출력 결과 형식
getType = "json"

url_cctv = f"https://openapi.its.go.kr:9443/cctvInfo?apiKey={key}&type={Type}&cctvType={cctvType}&minX={minX}&maxX={maxX}&minY={minY}&maxY={maxY}&getType={getType}"

response = urllib.request.urlopen(url_cctv)

json_str = response.read().decode("utf-8")

json_object = json.loads(json_str)

cctv_play = pd.json_normalize(json_object["response"]["data"], sep=',')
################################################################################

# 길이 ... 제한 해제
# pd.set_option("display.max_rows", None)  # 모든 행 출력
# pd.set_option("display.max_colwidth", None)  # 긴 문자열도 잘리지 않게 설정

# CCTV 링크 확인
# print(cctv_play["cctvurl"].head(5))
# print(cctv_play["cctvname"].head(5))
# len_cctv = len(cctv_play["cctvurl"])
# print(f"CCTV 총 개수 : {len_cctv}")

# 이미지 저장 폴더 생성
save_dir = "cctv/data"
if not os.path.exists(save_dir):
    os.makedirs(save_dir)

# 이미지 수집 단위 설정
interval_get_time = 5

# 이미지 수집 시간
last_save_time = time.time()

# CCTV 14번 영상 설정
test_url = cctv_play["cctvurl"][14]

cap = cv2.VideoCapture(test_url)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

# print(f"기본 해상도: {int(width)} x {int(height)}")
# 기본 해상도: 720 x 480

# 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        cv2.namedWindow("VIDEO", cv2.WINDOW_NORMAL)
        # frame = cv2.resize(frame, (1280, 720))
        # frame = cv2.resize(frame, (1920, 1080))
        frame = cv2.resize(frame, (3840, 2160))
        # frame = cv2.resize(frame, (7680, 4320))
        cv2.imshow("VIDEO", frame)
        
        # 현재 시간 확인
        current_time = time.time()

        if current_time - last_save_time >= interval_get_time:
            now = datetime.now()
            date_str = now.strftime("%Y%m%d_%H%M%S")
            weekday = now.strftime("%A")
            # print(weekday[0:2]) # Fr
            week_2 = weekday[0:2]
            
            filename = f"{save_dir}/{date_str}_{week_2}.jpg"
            
            cv2.imwrite(filename, frame)
            print(f"이미지 저장 : {filename}")
        
            # 마지막 수집 시간 업데이트
            last_save_time = current_time
        
        # "q" 키를 눌러서 종료
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
        
cap.release()
cv2.destroyAllWindows()