import streamlit as st
import cv2
import pandas as pd
import plotly.express as px
from ultralytics import YOLO

# annotated_frame 변수를 만들어서 영상으로 출력

# 0. Streamlit 페이지 설정
st.set_page_config(layout="wide")
st.title("YOLO_STREAMLIT")

# 1. 모델로드
model = YOLO("yolo11n.pt")

# 2. 비디오 경로
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv050.stream/playlist.m3u8")

# 3. 프레임, 차트 출력 공간 초기화
frame_placeholder = st.empty()
chart_placeholder = st.empty()

# 4. 비디오 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        st.error("FRAME CHECK")
        break
    
    # 4-1. 객체 탐지
    results = model(frame)
    
    # 4-2. 탐지된 프레임 가져오기
    annotated_frame = results[0].plot()
    annotated_frame = cv2.cvtColor(annotated_frame, cv2.COLOR_BGR2RGB)
    
    # import pdb; pdb.set_trace()
    # 4-3. Streamlit에서 이미지 출력
    frame_placeholder.image(annotated_frame, channels="RGB", use_container_width=True)

    # 4-4. 탐지된 객체 리스트 생성
    detected_objects = [model.names[int(box.cls[0])] for box in results[0].boxes]

    # 4-5. 탐지된 객체 수 계산
    object_count = pd.DataFrame({"객체": detected_objects}).value_counts().reset_index()
    object_count.columns = ["객체", "수량"]
    
    import uuid
    # 4-6. Plotly를 통한 그래프 시각화
    fig = px.bar(object_count, x='객체', y='수량', title='탐지된 객체 통계', text_auto=True)
    chart_placeholder.plotly_chart(fig, use_container_width=True, key=str(uuid.uuid4()))