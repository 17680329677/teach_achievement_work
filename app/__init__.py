import os

from flask import Flask
from app.config import Config
from flask_cors import CORS
from app.utils.mysql import db
import app.handler as handler
from app.core.auth import jwt_init
from app.utils.logger import consoleHandler, fileHandler

from flask_login import LoginManager
#from kafka import KafkaConsumer, KafkaProducer
import logging



app = Flask(__name__, template_folder=os.path.join(os.getcwd(), 'templates'),
        static_folder=os.path.join(os.getcwd(), 'static'))
#配置
app.config.from_object(Config)
Config.init_app(app)

# 利用flask-cors解决跨域问题，/*允许所有域外请求通过
cors = CORS(app, resources={r"/*": {"origins": "*"}})
cors.init_app(app)  # 跨域初始化

db.init_app(app) #数据库初始化



#消息订阅
#app.kafka_producer = KafkaProducer(bootstrap_servers=app.config['KAFLKA_HOST'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#基础功能
from .api_1_0 import api as api_1_0_blueprint
app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

#校级管理员功能
from .api_1_0.sadmin import sadmin as api_1_0_sadmin_blueprint
app.register_blueprint(api_1_0_sadmin_blueprint, url_prefix='/api/v1.0/sadmin')

#院级管理员功能
from .api_1_0.cadmin import cadmin as api_1_0_cadmin_blueprint
app.register_blueprint(api_1_0_cadmin_blueprint, url_prefix='/api/v1.0/cadmin')

#教师功能
from .api_1_0.normal import normal as api_1_0_normal_blueprint
app.register_blueprint(api_1_0_normal_blueprint, url_prefix='/api/v1.0/normal')

#学生功能
from .api_1_0.student import student as api_1_0_student_blueprint
app.register_blueprint(api_1_0_student_blueprint, url_prefix='/api/v1.0/student')

#jwt
jwt = jwt_init()
jwt.init_app(app)
app.logger.addHandler(consoleHandler)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers.extend(gunicorn_logger.handlers)
    app.logger.addHandler(fileHandler)
    app.logger.setLevel(gunicorn_logger.level)