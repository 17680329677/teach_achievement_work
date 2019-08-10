# 系统的配置信息
import os
from datetime import timedelta


class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'THE_KEY_THAT_HARD_TO_GESS'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@127.0.0.1/teach_achievement'

    MYSQL_USER = 'root'  # 数据库用户名
    MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD') or ''  # 数据库密码
    MYSQL_HOST = 'localhost'  # ip or host
    MYSQL_PORT = 3306  # 数据库端口
    MYSQL_DATABASE = 'teach_achievement'  # 数据库名称

    JWT_AUTH_URL_RULE = '/login'
    JWT_ALGORITHM = 'HS256'
    JWT_LEEWAY = timedelta(seconds=300)
    JWT_VERIFY_CLAIMS = ['signature', 'exp', 'nbf', 'iat']
    JWT_NOT_BEFORE_DELTA = timedelta(seconds=0)
    JWT_EXPIRATION_DELTA = timedelta(seconds=3600 * 24 * 30 * 12)
    JWT_REQUIRED_CLAIMS = ['exp', 'iat', 'nbf']
    JWT_AUTH_HEADER_PREFIX = 'bearer'
    # 用户登录接口已由flask-jwt默认定义好，默认路由是"/auth"，可以在配置文件中配置:
    # JWT_AUTH_URL_RULE = '/login'
    # 修改登录接口路由为'/login'
    # 需要注意的是，登录接口的传值要使用 application/json 形式

    CAPTCHA_EXPIRE = 300

    #文件路径
    UPLOAD_PATH = os.path.abspath('files/uploads')  # 上传文件路径


    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #kaflka
    # KAFLKA_HOST = ["127.0.0.1:17095", ]
    # KAFLKA_TOPIC = "teach_achievement_send_topic"



    @staticmethod
    def init_app(app):
        pass


if not os.path.exists(Config.UPLOAD_PATH):
    os.mkdir(Config.UPLOAD_PATH)



# 'mysql+mysqlconnector://root:123456@39.96.44.243/teach_achievement'
# 反向生成models.py : sqlacodegen mysql+mysqlconnector://root:@127.0.0.1/teach_achievement > new_models.py


# class DevelopmentConfig(Config):
#     DEBUG = True
#     MAIL_SERVER = 'smtp.163.com'
#     MAIL_PORT = 25
#     MAIL_USE_TLS = True
#     MAIL_USERNAME = 'laobahepijiu@163.com'
#     MAIL_PASSWORD = 'DHZ19960618'
#
#
# class TestingConfig(Config):
#     TESTING = True
#
#
# class ProductionConfig(Config):
#     pass
#
# # config字典注册了不同配置环境
# Config = {
#     'development': DevelopmentConfig,
#     'testing': TestingConfig,
#     'production': ProductionConfig,
#     'default': DevelopmentConfig
# }


# basedir = os.path.abspath(os.path.dirname(__file__))

# if __name__ == '__main__':
#     print(basedir)

