# save this as app.py
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
    
# CMD
    # set FLASK_APP=app1.py && flask run
    # 환경 변수를 파일명으로 명시해주고 명령어 실행

# VSCode Terminal
    # python app1.py
    # 파일 경로 위치로 이동 후 명령어 실행
