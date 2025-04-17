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
```
# log 파일 생성 확인 방법
Yolo Train => runs/detect/train/events.out.tfevents.1744182544.2AT.1604

# Tensorboard 설치
pip install tensorboard

# Tensorboard 실행(CMD)
tensorboard --logdir="C:/Users/Administrator/Desktop/ai/runs/detect/train"
```

- - -

**<p>$\it{\large{\color{#DD6565}25.04.10.목}}$</p>**
✅ 1차 발표 안내 (2025.04.11. 금)
```
발표 시작 : 오후 3시 (15:00)

발표 시간 : 팀당 15분 내외

질의응답 : 모든 인원은 발표 후 질문 1개 이상 필수

발표 순서 : 목요일 강의 종료 전 까지 전달
```

## 🔍 `visualize=True` 시각화 스테이지 분석
<p align="left">
  <img src="https://github.com/user-attachments/assets/927a7a29-d8de-4cca-85d4-d5d348c80ffd" width="700">
</p>

```
visualize=True 옵션은 YOLO 모델의 추론 시 중간 레이어의 Feature Map(특징 맵) 을 이미지로 저장해주는 기능
모델 내부가 어떻게 입력 영상을 해석하고 있는지 시각적으로 확인
```

```
밝은 영역: 해당 위치에서 강한 activation (특징 반응) 이 있었음을 의미
어두운 영역: 모델이 관심을 덜 가지는 부분
중간 레이어는 저수준 특징(모서리, 색상 등), 깊은 레이어는 고수준 특징(객체 윤곽 등)을 포착함
주의: 밝은 activation이 있다고 해서 반드시 탐지된 객체가 있는 건 아님 (confidence, 후처리 기준 미달일 수 있음)
```

| Stage 범위         | 위치                      | 의미                           | 시각화 특징                                 |
|-------------------|---------------------------|--------------------------------|---------------------------------------------|
| `stage_0 ~ stage_4`  | 초기 Convolution Layer     | Edge, Corner 탐지               | 밝기 변화, 윤곽선 강조                        |
| `stage_5 ~ stage_10` | 중간 Layer (Backbone)      | 모양, 패턴 인식                 | 윤곽보다 내부 구조 표현                       |
| `stage_11 ~ stage_16`| Neck (FPN, PAN 등)         | Multi-scale Feature 강화        | 복잡하고 의미 있는 부분 강조                 |
| `stage_17 ~ stage_20`| Head (예측 전 단계)        | 객체 존재 위치/크기 판단         | 관심 객체의 중심 부분만 밝게 나옴             |


**<p>$\it{\large{\color{#DD6565}25.04.11.금}}$</p>**
✅ 팀 프로젝트 발표 진행(1차)
## 발표 순서
1. [4way](https://github.com/borasarang3/4way/tree/main)<br>
2. [Don`t Cross Line](https://github.com/Hj-1000/AI_Project)<br>
3. [JoyK](https://github.com/JoYoungKyu/team_project)<br>
- - -

**<p>$\it{\large{\color{#DD6565}25.04.14.월}}$</p>**
## github 프로젝트 관리
1. 프로젝트 설명
2. 환경 설치 내용
3. requirements.txt
4. 설치 프로세스
- - -

**<p>$\it{\large{\color{#DD6565}25.04.15.화}}$</p>**
## OpenAPI 활용
[UTIC](https://www.utic.go.kr/guide/utisRefCctv.do)<br>
- - -

**<p>$\it{\large{\color{#DD6565}25.04.16.수}}$</p>**
## github 내용 점검
- - -

**<p>$\it{\large{\color{#DD6565}25.04.17.목}}$</p>**
## 최종 프로젝트 발표 안내
### 25.04.18.금.16시 ~ 최종 프로젝트 발표
### 1. 발표 순서 정하기
### 2. 발표 시간 15분 ~
### 3. 질문 1개씩
### 4. ai.murbachovski@gmail.com => 발표 자료 전달
  ### 4-1. 발표 파일 이름 형식 => "조 이름_프로젝트 이름"
  ### 4-2. 25.04.18.금.15시 30분 까지 전달
- - -

**<p>$\it{\large{\color{#DD6565}25.04.18.금}}$</p>**
## 최종 프로젝트 발표
- - -

## 이메일
```
ai.murbachovski@gmail.com
```

