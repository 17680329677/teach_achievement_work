from flask import Flask
from config import Config
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app(config_name):

    app = Flask(__name__)
    # 利用flask-cors解决跨域问题，/*允许所有域外请求通过
    cors = CORS(app, resources={r"/*": {"origins": "*"}})
    app.config.from_object(Config[config_name])
    Config[config_name].init_app(app)

    db.init_app(app)
    cors.init_app(app)

    from .api_1_0 import api as api_1_0_blueprint
    app.register_blueprint(api_1_0_blueprint, url_prefix='/api/v1.0')

    from .api_1_0.sadmin import sadmin as api_1_0_sadmin_blueprint
    app.register_blueprint(api_1_0_sadmin_blueprint, url_prefix='/api/v1.0/sadmin')

    from .api_1_0.normal import normal as api_1_0_normal_blueprint
    app.register_blueprint(api_1_0_normal_blueprint, url_prefix='/api/v1.0/normal')

    return app



