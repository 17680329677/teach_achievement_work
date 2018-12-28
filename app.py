from flask import Flask
from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
# 利用flask-cors解决跨域问题，/*允许所有域外请求通过
cors = CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/getMsg')
def msg():
    response = {
        'msg': '测试发送数据给vue'
    }
    return jsonify(response)


if __name__ == '__main__':
    app.run()
