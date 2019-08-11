import os

from flask import Flask
from app.config import Config
import app.handler as handler
from flask_cors import CORS
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




#消息订阅
#app.kafka_producer = KafkaProducer(bootstrap_servers=app.config['KAFLKA_HOST'],value_serializer=lambda v: json.dumps(v).encode('utf-8'))

#注册各个模块蓝图
app.register_blueprint(handler.token_bp)  #auth handler


app.register_blueprint(handler.book_bp)
app.register_blueprint(handler.book_rank_bp)


app.register_blueprint(handler.certificate_info_bp)
app.register_blueprint(handler.certificate_rank_bp)


app.register_blueprint(handler.college_bp)
app.register_blueprint(handler.department_bp)


app.register_blueprint(handler.innovation_project_bp)
app.register_blueprint(handler.innovation_rank_bp)


app.register_blueprint(handler.invigilate_info_bp)
app.register_blueprint(handler.semester_info_bp)
app.register_blueprint(handler.course_bp)


app.register_blueprint(handler.teach_reform_paper_bp)


app.register_blueprint(handler.teach_reform_project_bp)
app.register_blueprint(handler.project_type_bp)
app.register_blueprint(handler.project_child_type_bp)
app.register_blueprint(handler.project_rank_bp)
app.register_blueprint(handler.project_change_record_bp)


app.register_blueprint(handler.student_bp)
app.register_blueprint(handler.distribution_info_bp)
app.register_blueprint(handler.class_info_bp)
app.register_blueprint(handler.distribution_desire_bp)
app.register_blueprint(handler.distribution_result_bp)


app.register_blueprint(handler.teacher_bp)
app.register_blueprint(handler.teacher_role_bp)
app.register_blueprint(handler.teacher_info_bp)
app.register_blueprint(handler.teacher_category_bp)
app.register_blueprint(handler.teacher_title_bp)
app.register_blueprint(handler.title_record_bp)


#jwt
jwt = jwt_init()
jwt.init_app(app)
app.logger.addHandler(consoleHandler)


if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers.extend(gunicorn_logger.handlers)
    app.logger.addHandler(fileHandler)
    app.logger.setLevel(gunicorn_logger.level)