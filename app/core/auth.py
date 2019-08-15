from flask_jwt import JWT, JWTError, logger
from werkzeug.security import safe_str_cmp, check_password_hash
from app import dao, service
from werkzeug.local import LocalProxy
from sqlalchemy.exc import OperationalError, IntegrityError, DataError
from flask import request, current_app, jsonify, _request_ctx_stack
from datetime import datetime
from collections import OrderedDict
import jwt
import time

def jwt_init():
    custom_jwt = JWT()

    @custom_jwt.authentication_handler
    def authenticate(**kwargs):
        login_type = kwargs.get('type', 'teacher')

        if login_type == 'teacher':

            # 教师登录
            try:
                account = kwargs.get('username', None) #教师工号或账号
                password = kwargs.get('password', None)
                teacher = dao.TeacherDao.get(query={'account': account, 'password': password})
                if not teacher:
                    raise JWTError('Bad Request', '账号或密码错误')
                return dict(teacher)
            except (OperationalError, IntegrityError ) as e:
                raise JWTError('Bad Request', str(e))

        else:
            # 学生登录
            try:
                number = kwargs.get('username', None) #学号
                password = kwargs.get('password', None)
                student = dao.StudentDao.get(query={'number': number, 'password': password})
                if not student:
                    raise JWTError('Bad Request', '学号或密码错误')
                return dict(student)
            except (OperationalError, IntegrityError ) as e:
                raise JWTError('Bad Request', str(e))


    @custom_jwt.jwt_payload_handler
    def jwt_payload(identity):
        return new_payload(identity)


    @custom_jwt.identity_handler
    def identity(payload):
        user = payload['identity']
        return user


    @custom_jwt.auth_response_handler
    def auth_response(access_token, identity):
        return jsonify({'code': 200, 'token': access_token.decode('utf-8'), 'user': dict(identity)})


    @custom_jwt.jwt_error_handler
    def jwt_error(error):
        logger.error(error)
        return jsonify(OrderedDict([
            ('code', 500),
            ('msg', error.description)
        ])), error.status_code, error.headers


    @custom_jwt.auth_request_handler
    def auth_request():
        data = request.get_json()
        _jwt = LocalProxy(lambda: current_app.extensions['jwt'])

        identity_data = _jwt.authentication_callback(**data)

        if identity_data:
            access_token = _jwt.jwt_encode_callback(identity_data)
            return _jwt.auth_response_callback(access_token, identity_data)
        else:
            raise JWTError('Bad Request', '用户或密码错误')

    return custom_jwt

# 生成token的新载荷
def new_payload(identity):

    # “exp”: 过期时间
    # “nbf”: 表示当前时间在nbf里的时间之前，则Token不被接受
    # “iss”: token签发者
    # “aud”: 接收者
    # “iat”: 发行时间

    iat = datetime.utcnow()  # 发行时间
    exp = iat + current_app.config.get('JWT_EXPIRATION_DELTA')  # 过期时间 3600*24*30*12 秒
    nbf = iat + current_app.config.get('JWT_NOT_BEFORE_DELTA')  # 表示当前时间在nbf里的时间之前，则Token不被接受
    return {'exp': exp, 'iat': iat, 'nbf': nbf, 'identity': dict(identity)}  # 有效用户信息载荷


def new_token(identity):
    secret = current_app.config['JWT_SECRET_KEY']
    algorithm = current_app.config['JWT_ALGORITHM']
    required_claims = current_app.config['JWT_REQUIRED_CLAIMS']

    payload = new_payload(identity)
    missing_claims = list(set(required_claims) - set(payload.keys()))

    if missing_claims:
        raise RuntimeError('Payload is missing required claims: %s' % ', '.join(missing_claims))

    headers = None

    return jwt.encode(payload, secret, algorithm=algorithm, headers=headers)

