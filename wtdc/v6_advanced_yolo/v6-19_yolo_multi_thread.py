from ultralytics import YOLO
import cv2
import threading
import timeit


# 비디오 경로 설정
video_file1 = "heatmap.mp4"
video_file2 = "wtdc/_data/track.mp4"
video_file3 = "heatmap-parking.mp4"
video_file4 = "heatmap.mp4"

# 모델 로드
model1 = YOLO("yolo11n.pt")
model2 = YOLO("yolov5nu.pt")
model3 = YOLO("yolov10n.pt")
model4 = YOLO("yolov9t.pt")

# 비디오 파일 처리 및 객체 추적 실행 함수
def run_tracker(filename, model, file_index):
    cap = cv2.VideoCapture(filename)
    
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
        
        model_name = model.ckpt_path
        print(model_name)
        # print(dir(model))
        
        cv2.putText(
            res_resized,
            f"FPS : {FPS}, model : {model_name}",
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
thread1 = threading.Thread(target=run_tracker, args=(video_file1, model1, 1), daemon=True)
# 스레드 생성
thread2 = threading.Thread(target=run_tracker, args=(video_file2, model2, 2), daemon=True)
thread3 = threading.Thread(target=run_tracker, args=(video_file3, model3, 3), daemon=True)
thread4 = threading.Thread(target=run_tracker, args=(video_file4, model4, 4), daemon=True)

# 스레드 실행
thread1.start()
thread2.start()
thread3.start()
thread4.start()

# 스레드 종료 대기
thread1.join()
thread2.join()
thread3.join()
thread4.join()

# 영상 화면에 FPS, 모델명 넣어주기 