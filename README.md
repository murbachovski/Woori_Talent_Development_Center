## 🎁우리인재개발원(우리컴퓨터아카데미)
```
교차로 교통 장애물 및 이벤트 감지 시스템 개발
```

## 🎁팀 현황
1. [JoyK](https://github.com/JoYoungKyu/team_project)<br>
2. [4way](https://github.com/borasarang3/4way/tree/main)<br>
3. [Don`t Cross Line](https://github.com/Hj-1000/AI_Project)<br>

## 🎁프로젝트 진행
<p align="center">
  <img src="https://github.com/user-attachments/assets/a48edc5f-2036-4fba-8f50-e482d6bb4d50" width="700">
</p>


## 🎁참고 문서
**OpenAPI 활용**<br>
[ITS 국가교통정보센터](https://its.go.kr/opendata/opendataList?service=cctv)<br>

**OpenAPI ITS 활용법**<br>
[고속도로 CCTV Open API 불러오기(ITS 국가교통정보센터)](https://s0ysauce.tistory.com/38)<br>

**AI 활용 사례**<br>
[교통량 측정 CCTV](https://www.mk.co.kr/news/politics/10847270)<br>

**예제 문제**<br>
🚩 [Google Machine Learning Crash Course - Precision & Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) <br>
🚩 [Google Machine Learning Crash Course - Classification: ROC and AUC](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) <br>

- - -
**<p>$\it{\large{\color{#DD6565}25.04.07.월}}$</p>**
**Original Image**<br>
<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/9a975c01-97eb-46e6-a755-3042c6919213" width="500" height="500" style="object-fit: cover;">
</div>

 **Background Image**(based on ChatGPT)<br>
<div style="display: flex; justify-content: space-between;">
  <img src="https://github.com/user-attachments/assets/1f34235a-210f-45a8-a544-366266fa65a4" width="500" height="500" style="object-fit: cover;">
</div>

**tips_for_best_training_results**<br>
[tips_for_best_training_results](https://docs.ultralytics.com/yolov5/tutorials/tips_for_best_training_results)<br>

- - -
**<p>$\it{\large{\color{#DD6565}25.04.08.화}}$</p>**
**Resuming Interrupted Trainings**<br>
[YOLO Train Parameter resume](https://docs.ultralytics.com/modes/train/#resuming-interrupted-trainings)<br>

**Transfer Learning with Frozen Layers**<br>
[YOLO Train Parameter freeze](https://docs.ultralytics.com/yolov5/tutorials/transfer_learning_with_frozen_layers/)<br>

**Pruning**<br>
[Model Pruning and Sparsity in YOLOv5](https://docs.ultralytics.com/yolov5/tutorials/model_pruning_and_sparsity/)<br>
<p align="left">
  <img src="https://github.com/user-attachments/assets/6257c65e-c700-4e30-83b8-32e9f5e33abd" width="700">
</p>

**Quantization**<br>
[Model Quantization](https://docs.ultralytics.com/guides/model-deployment-practices/#model-quantization)<br>
<p align="left">
  <img src="https://github.com/user-attachments/assets/7703ab83-7ccc-48b2-b7cc-79eea977c767" width="700">
</p>

**성능 지표 설명**<br>
```
F1-Confidence Curve
• F1 점수는 분류 모델의 성능을 나타내는 메트릭 중 하나로, 정밀도(Precision)와 재현율(Recall)의 조화 평균입니다.
• 1에 가까울수록 모델의 성능이 좋다는 것을 의미합니다.
```
- - -

**<p>$\it{\large{\color{#DD6565}25.04.09.수}}$</p>**
#### Precision and Recall
```
Precision(정밀도) : 모델의 Positive 중 실제 Positive 
Recall(재현율) : 실제 Positive 중 모델의 Positive
```

## 📝Precision-Recall 관련 문제

#### 객체 탐지 모델을 적용했더니 탐지된 객체는 대부분 정확하지만, 많은 실제 객체를 놓치는 경우
```
✅ 정답: Precision ↑, Recall ↓
✅ 해결 방법: Recall을 높이기 위해 Confidence Threshold를 낮추고 탐지 범위를 확대해야 한다.
```

#### 탐지 시스템에서 거의 모든 사람을 탐지할 수 있지만, 실제 사람이 아닌 그림자나 마네킹도 사람으로 오탐하는 경우
```
✅ 정답: Precision ↓, Recall ↑
✅ 해결 방법: Confidence Threshold를 높이고, Hard Negative Mining을 적용
```

#### 탐지된 객체 중 상당수가 오탐이며, 실제 객체도 잘 탐지되지 않는 경우가 발생
```
✅ 정답: Precision ↓, Recall ↓
✅ 해결 방법: 데이터셋을 개선하고, 모델을 추가 학습해야 한다. 또한, NMS와 Confidence Threshold를 적절히 조정하여 탐지 성능을 개선
```

#### 모델이 적용된 후 탐지된 객체는 대부분 정확하고, 실제 객체도 놓치지 않고 탐지
```
✅ 정답: Precision ↑, Recall ↑
✅ 설명: 이상적인 모델이며, 성능이 최적화된 상태
```

## 💡관련 용어 설명
#### Hard Negative Mining
```
객체 탐지 모델에서 오탐(False Positive)이 많은 경우, 특히 배경을 객체로 잘못 인식하는 문제를 해결하는 기법
즉, 모델이 헷갈려하는 "어려운 배경(하드 네거티브)"을 학습 데이터로 추가하여 성능을 개선하는 방법
```

## 💡Tensorboard 확인
#### Tensorboard
```
# log 파일 확인
Yolo Train => runs/detect/train/events.out.tfevents.1744182544.2AT.1604
# Tensorboard 설치
pip install tensorboard
# Tensorboard 실행(CMD)
tensorboard --logdir="C:/Users/Administrator/Desktop/ai/runs/detect/train"
```
