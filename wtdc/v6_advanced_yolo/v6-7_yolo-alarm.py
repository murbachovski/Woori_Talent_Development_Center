from ultralytics import solutions
import cv2

# 비디오 로드
cap = cv2.VideoCapture("http://210.99.70.120:1935/live/cctv014.stream/playlist.m3u8")

# 이메일 인증 정보
from_email = "ai.murbachovski@gmail.com"
password = "hqsu venx bbba zokx"
to_email = "ai.murbachovski@gmail.com"

# 보안 알림 시스템 객체 생성
security = solutions.SecurityAlarm(
    model='yolo11n.pt',
    record=1, # 탐지된 객체 수가 record 수 이상일 때 이메일 전송합니다.
    show=True
)

# 이메일 인증
security.authenticate(from_email, password, to_email)

# 프레임 처리
while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("프레임 읽기 실패")
        break
    
    # 객체 탐지 수행
    result_frame = security(frame)

    # ESC 키를 누르면 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 종료 처리
cap.release()
cv2.destroyAllWindows()

# https://myaccount.google.com/people-and-sharing?gar=WzJd&hl=ko&utm_source=OGB&utm_medium=act