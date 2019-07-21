# 系统的配置信息
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'THE_KEY_THAT_HARD_TO_GESS'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:@127.0.0.1/teach_achievement'
    # 'mysql+mysqlconnector://root:123456@39.96.44.243/teach_achievement'
    # 反向生成models.py : sqlacodegen mysql+mysqlconnector://root:@127.0.0.1/teach_achievement > new_models.py
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #kaflka
    KAFLKA_HOST = ["127.0.0.1:17095", ]
    KAFLKA_TOPIC = "teach_achievement_send_topic"

    @staticmethod
    def init_app(app):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    MAIL_SERVER = 'smtp.163.com'
    MAIL_PORT = 25
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'laobahepijiu@163.com'
    MAIL_PASSWORD = 'DHZ19960618'


class TestingConfig(Config):
    TESTING = True


class ProductionConfig(Config):
    pass

# config字典注册了不同配置环境
Config = {
    'development': DevelopmentConfig,
    'testing': TestingConfig,
    'production': ProductionConfig,
    'default': DevelopmentConfig
}


# if __name__ == '__main__':
#     print(basedir)