## 🎁우리인재개발원(우리컴퓨터아카데미)
```
교차로 교통 장애물 및 이벤트 감지 시스템 개발
```

## 🎁프로젝트 진행 프로세스
```
1. 타임 테이블 작성 (세부 일정 확정)
2. GitHub 생성 및 브랜치 전략 수립
3. main, dev, feature/각 팀별 작업
4. README.md 작성 (프로젝트 개요, 목표, 팀원 역할 포함)
5. 주제 선정 (교차로 장애물 감지의 세부 주제 확정)
6. 팀장 선정 및 역할 분배
7. 데이터 수집 및 전처리 담당
8. 모델 설계 및 학습 담당
9. 시스템 통합 및 구현 담당
10. 발표 자료 제작 및 문서화 담당
11. 1차 발표 (4월 11일)
12. 중간 진행 상황 보고
13. 최종 발표 (4월 18일)
14. 최종 모델 및 결과 발표

<추가 사항>
기술 스택 및 개발 환경 설정
사용할 프로그래밍 언어, 프레임워크, 라이브러리 결정
개발 환경(로컬/클라우드, Docker 사용 여부 등) 정리
이슈 트래킹 및 일정 관리
Jira, Trello, GitHub Projects 등을 활용한 일정 및 작업 관리
테스트 및 검증 프로세스 추가
테스트 기준 및 성능 평가 방법 정의
실시간 모니터링 및 배포 전략
시스템 운영 및 실시간 장애 감지 방안
리스크 관리 및 백업 계획
데이터 손실 방지를 위한 백업 방법
주요 리스크(데이터 부족, 모델 학습 문제 등) 사전 대응 방안
사용자 피드백 및 개선 사항 반영
1차 발표 후 피드백 수집 및 정리
추가 개선 작업 진행 여부 결정
```

## 🎁타임 테이블(예시
<p align="center">
  <img src="https://github.com/user-attachments/assets/25babc94-10e1-473f-9fee-11ed3c406d91" width="600">
</p>

## 🎁프로젝트 일정 수립(예시

| 날짜        | 내용                          |
|------------|-----------------------------|
| 4월 2~4일  | 팀 주제 브레인스토밍 & 확정   |
| 4월 5~7일  | 데이터 수집 및 전처리        |
| 4월 8~10일 | 모델 선정 및 실험 시작       |
| 4월 11일   | 1차 발표 (중간 진행 상황 공유) |
| 4월 12~16일 | 모델 개선 및 최적화         |
| 4월 17일   | 최종 발표 리허설             |
| 4월 18일   | 🎤 최종 발표                 |

위 일정에 따라 프로젝트를 진행하며, 각 단계별 진행 상황을 지속적으로 공유할 예정입니다.

## 🎁기술 스택 & 협업 환경
```
프레임워크: TensorFlow, PyTorch
개발 도구: Python, OpenCV, YOLO
데이터셋 관리: Google Drive, Kaggle, Git LFS
버전 관리: GitHub (브랜치 전략 활용)
협업 도구: Notion, Slack
```

## 💡발표 준비
```
발표 내용 개요 정리 (기술적/비기술적 내용 균형 잡기)
데모 영상 또는 실시간 시연 준비
예상 질문 리스트 정리 후 Q&A 준비
```

## 🎁테스트 및 평가
```
프로젝트 성능 평가 지표 확정 (정확도, 속도, False Positive Rate 등)
실제 교차로 데이터를 활용한 테스트 계획 수립
```

## 🎁팀 현황
1. [A조](https://github.com/murbachovski/Woori_Talent_Development_Center/edit/team/README.md)<br>
2. [B조](https://github.com/murbachovski/Woori_Talent_Development_Center/edit/team/README.md)<br>
3. [C조](https://github.com/murbachovski/Woori_Talent_Development_Center/edit/team/README.md)<br>
4. [D조](https://github.com/murbachovski/Woori_Talent_Development_Center/edit/team/README.md)<br>

## 🎁구성원
```
팀장: 김OO
팀원: 이OO, 박OO, 최OO
```

## 🎁설명(예시
```
YOLO를 활용한 교차로 불법 주차 관리 시스템 개발
```

## 🎁환경 셋팅(예시
The code requires python>=3.9 and we use torch==1.10.2 and torchvision==0.11.3. To visualize the results, matplotlib>=3.5.1 is also required.
```
python>=3.7
pytorch==1.10.2
torchvision==0.11.3
matplotlib==3.5.1
```

## 🎁환경 설치(예시
```
pip install -r requirements.txt
```

## 🎁실행(예시
```
cd team_project
python3 app.py
```

## 💡CCTV 접근
1. [카카오맵](https://map.kakao.com/?nil_profile=title&nil_src=local)
<p align="center">
  <img width="1081" alt="Image" src="https://github.com/user-attachments/assets/2be59a8d-c2cc-4867-9db1-d255f4de3303" width="300">
</p>

### 접근 방법
```
카카오맵 CCTV 접근 => 소스코드(F12) 확인 => 비디오 링크 복사 => cv2.CaptureVideo() 적용 => 영상 스트리밍
```

### 예시 링크
```
cap = cv2.VideoCapture("https://cctvsec.ktict.co.kr/6246/cCCtjN+N+EnDEdCu9wHS00X5iOMXIc41FwpwasljdCsrysX/jGzlP6b54WADcjaY")
```

## 💡YOLO custom_datasets 경로 셋팅
```
coco8.yaml => path : coco8 폴더 경로, train : train 폴더 경로, val : val 폴더 경로
model.train(data='coco8.yaml 파일 경로')
```

## 💡Background images
<img src="https://github.com/user-attachments/assets/052d795a-8361-4905-b325-8124e7ba729d" width="600">

```
FP => 거짓 탐지 => 오탐을 줄일 수 있다.
```
## 💡Data Augmentation
<p align="center">
  <img src="https://github.com/user-attachments/assets/81c866a3-c39d-4cb4-89d6-a7bc818e7a65" width="600">
</p>

## 💡파이썬 경고음 넣기
[더미 경고음 사이트](https://pixabay.com/ko/sound-effects/search/%EA%B2%BD%EA%B3%A0%EC%9D%8C/)

```
# MAC
import os
os.system(afplay ./alarm.mp3)

# MAC(비동기)
import subprocess
subprocess.Popen(["afplay", "./alarm.mp3"])

# Winodws
pip install playsound
from playsound import playsound
playsound('./alarm.mp3')
```

## 💡requirements.txt 만들기
```
1. pip install pipreqs 설치
2. 프로젝트 폴더 경로 이동
3. pipreqs --savepath ./requirements.txt
4. 저장 경로 확인
```

## 💡Twilio 활용하여 Python으로 문자 알림 보내기
[Twilio](https://www.twilio.com/en-us)
```
Twilio 회원가입 후
번호 등록 및 생성 후 코드 변환하여 사용
```

<p align="center">
  <img src="https://github.com/user-attachments/assets/bd68c8dd-626e-475c-97fc-a50108abdd10" width="1000">
</p>

## 💡README.md 파일 작성법 및 소개
```
https://gist.github.com/ihoneymon/652be052a0727ad59601
```

## 💡성능 평가 용어 설명👀
#### Precision(정밀도)

```
모델의 Positive로 판정한 것 중, 실제 Positive 비율
```

#### Recall(재현율)

```
실제 Positive 중 모델의 Positive 비율
```

#### F1-score

<p align="center">
  <img src="https://github.com/user-attachments/assets/4fdffc5c-ae29-4dab-8ec0-5f80e025d268" width="300">
</p>

```
Precision과 Recall의 조화평균
```

#### 조화평균(여러 값의 평균을 구할 때, 작은 값이 상대적으로 더 큰 영향을 주는 평균 방식)
```
1. Precision과 Recall 중 하나라도 낮으면 F1-score도 낮아짐
  예를 들어 Precision = 90, Recall = 10이면 일반 평균은 50이지만, 조화평균을 쓰면 F1-score ≈ 18.2로 낮아짐 → 한쪽이 낮으면 전체 성능도 낮게 반영

2. 둘의 균형을 맞추는 데 효과적
  Precision이 높지만 Recall이 낮거나, 그 반대인 경우를 방지

3. 극단적인 값을 줄여줌
  예를 들어, 일반 평균(산술평균)은 극단적인 값(예: 한쪽이 100, 한쪽이 1)에 영향을 많이 받지만, 조화평균은 이를 보완
```

#### ROC Curve
<p align="center">
  <img src="https://github.com/user-attachments/assets/91d7948a-ec7e-483a-b8eb-e0e1a53e0f60" width="300">
</p>

```
✅ ROC Curve는 모델의 전체적인 분류 성능을 평가하는 곡선
✅ FPR vs. TPR의 관계를 나타내며, 좌상단에 가까울수록 좋은 모델
✅ AUC 값이 클수록 좋은 성능을 의미 (1에 가까울수록 우수)
```

#### 참고 링크
🚩 [Precision-Recall vs. ROC Curve - CosmicCoding](https://cosmiccoding.com.au/tutorials/pr_vs_roc_curves/) <br>
🚩 [Receiver Operating Characteristic (ROC) - Wikipedia](https://en.wikipedia.org/wiki/Receiver_operating_characteristic) <br> 
🚩 [Confusion Matrix - Wikipedia](https://en.wikipedia.org/wiki/Confusion_matrix) <br>
🚩 [ROC Curve & AUC 설명 - Dream2Reality 블로그](https://dream2reality.tistory.com/9) <br>
🚩 [머신러닝 성능 측정 방법 - Meme2515 블로그](https://meme2515.github.io/machine_learning/performance_measurement/) <br>
🚩 [분류 성능 지표 (Precision, Recall) - AI-Com 블로그](https://ai-com.tistory.com/entry/ML-%EB%B6%84%EB%A5%98-%EC%84%B1%EB%8A%A5-%EC%A7%80%ED%91%9C-Precision%EC%A0%95%EB%B0%80%EB%8F%84-Recall%EC%9E%AC%ED%98%84%EC%9C%A8) <br>

#### 예제 문제
🚩 [Google Machine Learning Crash Course - Precision & Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) <br>
🚩 [Google Machine Learning Crash Course - Classification: ROC and AUC](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) <br>

## 💡Precision과 Recall의 경우의 수
| Precision (정밀도) | Recall (재현율) | 의미                                       |
|-------------------|---------------|------------------------------------------|
| 높음               | 높음            | 이상적인 모델 (오탐과 미탐이 적음)              |
| 높음               | 낮음            | 탐지를 신중하게 하지만 많은 객체를 놓침 (미탐 증가) |
| 낮음               | 높음            | 많은 객체를 탐지하지만 오탐이 많음 (오탐 증가)     |
| 낮음               | 낮음            | 모델 성능이 매우 나쁨 (오탐과 미탐이 많음)        |


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

#### 💡Base64 인코딩
<p align="center">
  <img src="https://github.com/user-attachments/assets/84a0bfe9-ce05-46cc-84f1-ac3343aa3c73" width="600">
</p>

```
문자열을 다시 디코딩하면 이미지로 돌아옵니다.
```

#### 💡이메일
```
ai.murbachovski@gmail.com
```
