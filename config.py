# 系统的配置信息
import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = 'DHZAZY1216'
    SQLALCHEMY_DATABASE_URI = 'mysql+mysqlconnector://root:123456@localhost/teach_achievement'
    SQLALCHEMY_COMMIT_ON_TEARDOWN = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False

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