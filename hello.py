from flask import Flask, request
from flask_cors import CORS
import json
import satk

s = satk.news_classifier.Pipeline()


app = Flask(__name__)
CORS(app)

@app.route('/test')
def test():
    print('hello')
    # data = request.get_json(silent=True)
    # print(data['aa']) #123
    return 'Hello, World'

@app.route('/login', methods=['POST', 'GET'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        print(data['news'])
    else:
        print("get method")
    return s(data['news'])