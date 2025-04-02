from ultralytics import YOLO
import cv2
from flask import Flask, Response

# Flask 애플리케이션 초기화
app = Flask(__name__)

# 비디오 스트리밍 함수 정의
def generate_frame():
    # cap = cv2.VideoCapture("C:/Users/Administrator/Desktop/ai/wtdc/_data/track.mp4")
    cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv006.stream/playlist.m3u8")
    
    while True:
        success, frame = cap.read()
        if not success:
            print("프레임 확인")
            break
        
        # 프레임을 JPEG 형식으로 인코딩
        _, buffer = cv2.imencode('.jpg', frame)
        
        # 인코딩된 이미지를 바이트 형태로 변환
        frame_bytes = buffer.tobytes()
        
        # 실시간으로 비디오 스트리밍 데이터 전송
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
        
    cap.release()
    
# Flask 라우트 정의
@app.route('/')
def video_feed():
    # 비디오 스트리밍 제공
    return Response(generate_frame(), mimetype='multipart/x-mixed-replace; boundary=frame')

# 애플리케이션 실행
if __name__ == "__main__":
    # Flask 서버를 실행
    app.run(host="0.0.0.0", port=5000, debug=True)