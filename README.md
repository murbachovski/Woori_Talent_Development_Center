## 🎁우리인재개발원(우리컴퓨터아카데미)
```
교차로 다중 이벤트 감지 시스템 개발
```

## 🎁프로젝트 진행
<p align="center">
  <img src="https://github.com/user-attachments/assets/a48edc5f-2036-4fba-8f50-e482d6bb4d50" width="700">
</p>

## 🎁프로그램 진행 예상도
```
1. 데이터 수집
  1-1. ITS OpenAPI 활용
  1-2. CCTV 영상 검수
  1-3. 1초 / 10초 / 1분 / 10분 각각 단위로 영상에서 이미지 수집
  1-4. Train 1000 / Val 400 / Test 100 / Background / 100
2. 데이터 라벨링
  2-1. Roboflow
3. 데이터 전처리
  3-1. 밝기, 대비 적용
  3-2. Background Image 생성
4. 데이터 검수
  4-1. 라벨링 검수 및 체크
5. 모델 학습
  5-1. Ultralytics 공식 문서 확인하여 훈련 횟수 선정 및 파라미터 점검
6. 모델 평가
  6-1. 성능 지표 확인
7. 모델 적용
  7-1. 실제 환경 적용 후 모니터링
  7-2. 결과 영상 수집
  7-3. 피드백 및 수정 사항 정리
```

## 🎁참고 문서
**OpenAPI 활용**<br>
[ITS 국가교통정보센터](https://its.go.kr/opendata/opendataList?service=cctv)<br>

**OpenAPI ITS 활용법**<br>
[고속도로 CCTV Open API 불러오기(ITS 국가교통정보센터)](https://s0ysauce.tistory.com/38)<br>

**AI 활용**<br>
[교통량 측정 CCTV](https://www.mk.co.kr/news/politics/10847270)<br>

**예제 문제**<br>
🚩 [Google Machine Learning Crash Course - Precision & Recall](https://developers.google.com/machine-learning/crash-course/classification/accuracy-precision-recall) <br>
🚩 [Google Machine Learning Crash Course - Classification: ROC and AUC](https://developers.google.com/machine-learning/crash-course/classification/roc-and-auc) <br>

**Background Image**<br>
<p align="center">
  <img src="https://github.com/user-attachments/assets/1f34235a-210f-45a8-a544-366266fa65a4" width="700">
</p>
