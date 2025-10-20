# app.py
from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    # Dòng text mong muốn
    return 'Xin chào! Ứng dụng này đã được triển khai bằng OpenShift GitOps.'

if __name__ == '__main__':
    # Sử dụng cổng mặc định của OpenShift
    port = int(os.environ.get('PORT', 8080))
    app.run(host='0.0.0.0', port=port)

