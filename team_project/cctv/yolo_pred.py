import urllib
import json
import pandas as pd
import cv2
from ultralytics import YOLO

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

# CCTV 14번 영상 설정
test_url = cctv_play["cctvurl"][14]

cap = cv2.VideoCapture(test_url)
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)

model = YOLO("C:/Users/Administrator/Desktop/ai/runs/detect/train/weights/best.pt")

# 비디오 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    
    if success:
        results = model(frame)[0]
        results = results.plot()
        
        cv2.namedWindow("VIDEO", cv2.WINDOW_NORMAL)
        # frame = cv2.resize(frame, (1280, 720))
        # frame = cv2.resize(frame, (1920, 1080))
        # frame = cv2.resize(frame, (3840, 2160))
        # frame = cv2.resize(frame, (7680, 4320))
        cv2.imshow("VIDEO", results)
        
        # "q" 키를 눌러서 종료
        if cv2.waitKey(10) & 0xFF == ord("q"):
            break
        
cap.release()
cv2.destroyAllWindows()