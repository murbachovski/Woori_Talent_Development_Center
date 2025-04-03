from dash import Dash, html, dcc # => 대시보드 웹을 만들기 위한
from dash.dependencies import Input, Output # => 콜백을 통해 업데이트
import plotly.graph_objs as go # => 그래프 시각화
import base64 # => 이미지 인코딩을 위한
import cv2
from ultralytics import YOLO
from datetime import datetime # => 현재 시간 가져오기

# 모델 로드
model = YOLO('yolo11n.pt')

# 데이터 저장할 리스트
x_date = []
y_data = []

# Dash 애플리케이션 초기화
app = Dash(__name__)

# 대시보드 레이아웃 정의
app.layout = html.Div([
    html.H1("Dash Yolo 탐지 대시보드",
            style={"textAlign": "center"}),
    html.Div([
        html.Img(id="live-detection-image",
                 style={"width": "80%", "margin": "auto", "display": "block"})
    ]),
    # 그래프
    dcc.Graph(id="Dash-Yolo-Graph",
              style={"height": "400px"}),
    dcc.Interval(
        id="update-interval",
        interval=1000, # => 1초 마다 업데이트
        n_intervals=0 # => 초기 실행 횟수
    )
])

# 비디오 경로 설정
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv020.stream/playlist.m3u8")

# 콜백 함수 정의 => 화면, 그래프 업데이트를 하기 위해서
# Dash는 특정 입력이 발생하면 출력을 자동으로 업데이트해줌!!
@app.callback(
    [
        Output("live-detection-image", "src"),
        Output("Dash-Yolo-Graph", "figure"),
    ],
    [
        Input("update-interval", "n_intervals")
    ]
)

def update_frame(n_intervals):
    global cap
    
    # 프레임 읽기 및 처리
    success, frame = cap.read()
    if not success:
        print("FRAME CHECK")
        return None, go.Figure()
    
    # 객체 탐지 수행
    results = model(frame)
    
    # 객체 탐지 수 계산
    num = len(results[0].boxes)
    
    # 탐지 결과를 이미지에 표시
    annotated_frame = results[0].plot()
    
    # 이미지 => 인코딩 => Base64
    _, buffer = cv2.imencode('.jpg', annotated_frame)
    frame_base64 = base64.b64encode(buffer).decode()
    
    # 현재 시간 가져오기
    current_time = datetime.now().strftime("%Y%m%d_%H:%M%S")
    
    # 시간과 탐지된 객체 수를 추가 저장
    x_date.append(current_time)
    y_data.append(num)
    
    # 실시간 그래프 데이터 생성
    figure = {
        'data': [
            go.Scatter(
                x=x_date, # => 시간
                y=y_data, # => 탐지된 객체 수
                mode='lines+markers',
                marker={'color': 'red'}
            )
        ],
        'layout': go.Layout(
            title="실시간 탐지 수 변화", # => 그래프 제목
            xaxis={"title": "시간"}, # => x축
            yaxis={"title": "탐지 수", 'dtick': 1}, # => y축
            template="plotly_white" # 그래프 스타일
        )
    }
    
    return f"data:image/jpeg;base64,{frame_base64}", figure

# 앱 실행
if __name__ == "__main__":
    # app.run_server() # => Dash 서버 실행
    app.run()