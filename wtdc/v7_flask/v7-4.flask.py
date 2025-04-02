from ultralytics import YOLO
import cv2
from flask import Flask, Response

# 1. Flask 애플리케이션 초기화
app = Flask(__name__)

# 2. YOLO 모델 로드
model = YOLO('yolo11n.pt')

# 3. 비디오 스트리밍 함수 정의
def generate_frame():
    
    # 비디오 경로 설정
    cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv006.stream/playlist.m3u8")
    
    # 3-1. 프레임 확인
    while True:
        success, frame = cap.read()
        if not success:
            print("FRAME CHECK")
            break
        
        # 3-2. 객체 탐지
        results = model(frame)
        
        # 3-3. 탐지 표시
        annotated_frame = results[0].plot()
        
        # 3-4. 객체 수 추출
        detected_object_count = len(results[0].boxes)
        
        # 3-5. 상태 메시지 정의
        status = f"COUNT : {detected_object_count}"
        if detected_object_count <= 0:
            status += "=> Normal"
            color = (0, 0, 0) # Black
        elif detected_object_count <= 3: 
             status += "=> Warning"
             color = (255, 0, 0) # Blue
        else:
            status += "=> Danger"
            color = (0, 0, 255) # Red
            
        # 3-6. 상태 메시지 화면 추가
        cv2.putText(
            annotated_frame,
            f"{status}",
            (10, 10),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            color,
            2
        )
        
        # 3-7. 프레임2(to)인코딩
        _, buffer = cv2.imencode('.jpg', annotated_frame)
        
        # 3-8. 인코딩2(to)바이트
        frame_bytes = buffer.tobytes()
        
        # 3-9. 데이터 전송(yield)
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n'
               )
        
    # 3-10. 비디오 해제
    cap.release()
    
# 4. Flask 라우트 정의
@app.route('/')
def video_feed():
    return Response(generate_frame(), mimetype="multipart/x-mixed-replace; bounday=frame")

# 5. 애플리케이션 실행
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)