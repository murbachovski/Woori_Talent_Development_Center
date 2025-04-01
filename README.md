### 초기 셋팅
```
1. Anaconda 설치
https://repo.anaconda.com/archive/
버전 : Anaconda3-2024.10-1-Windows-x86_64.exe ==> 설치

2. 가상환경 생성
conda create -n "Youre_env_name" python=3.9

3. 가상환경 실행
conda activate py39
```

### 라이브러리 설치
```
1. pip install pipreqs 설치
2. 프로젝트 폴더 경로 이동
3. pipreqs --savepath ./requirements.txt
4. 저장 경로 확인
5. pip install -r ./requirements.txt
```
