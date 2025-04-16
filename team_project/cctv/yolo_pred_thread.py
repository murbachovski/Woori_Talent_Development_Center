import urllib
import json
import pandas as pd
import cv2
from ultralytics import YOLO
import threading
import timeit
import os


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

model_v1 = YOLO("C:/Users/Administrator/Desktop/ai/runs/detect/train/weights/best.pt")
model_v2 = YOLO("C:/Users/Administrator/Desktop/ai/runs/detect/train/weights/last.pt")

# 비디오 파일 처리 및 객체 추적 실행 함수
def run_tracker(test_url, model, file_index):
    cap = cv2.VideoCapture(test_url)
    
    # 비디오가 열려 있는 동안 프레임을 반복해서 처리
    while cap.isOpened():
        success, frame = cap.read()
        if not success:
            break
        
        start_time = timeit.default_timer()
        
        # 객체 탐지
        results = model.track(frame, persist=True)
        res_plotted = results[0].plot() 
        
        end_time = timeit.default_timer()
        
        FPS = int(1./(end_time - start_time))
        
        # 창 크기 조절
        res_resized = cv2.resize(res_plotted, (640, 480))
        
        model_name = model.model_name
        real_name = os.path.basename(model_name)
        print(real_name)
        # print(dir(model))
        
        cv2.putText(
            res_resized,
            f"FPS : {FPS}, model : {real_name}",
            # f"FPS : {FPS}",
            (30, 30),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2,
            cv2.LINE_AA
        )
        
        # 화면 표시
        cv2.imshow(f"Tracking_Multi_YOLO{file_index}", res_resized)
        
        # q 키 눌러서 종료
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        
    cap.release()
    cv2.destroyAllWindows()

# 스레드 생성
thread1 = threading.Thread(target=run_tracker, args=(test_url, model_v1, 1), daemon=True)
# 스레드 생성
thread2 = threading.Thread(target=run_tracker, args=(test_url, model_v2, 2), daemon=True)

# 스레드 실행
thread1.start()
thread2.start()

# 스레드 종료 대기
thread1.join()
thread2.join()