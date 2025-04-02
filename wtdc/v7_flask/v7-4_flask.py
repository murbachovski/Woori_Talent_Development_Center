from ultralytics import YOLO
import cv2
from flask import Flask, Response

# 실습 : Flask 웹 영상에서 상태 메시지 정의

# 1. Flask 애플리케이션 초기화
# 2. YOLO 모델 로드
# 3. 비디오 스트리밍(처리) 함수 정의
# 3-1. 프레임 확인
# 3-2. 객체 탐지
# 3-3. 탐지 표시
# 3-4. 객체 수 추출
# 3-5. 상태 메시지 정의
# 3-6. 상태 메시지 화면 추가
# 3-7. 프레임을 인코딩
# 3-8. 인코딩을 바이트
# 3-9. 데이터 전송(yield)
# 4. Flask 라우트 정의
# 5. 애플리케이션 실행