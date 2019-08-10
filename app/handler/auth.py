from flask import Blueprint, jsonify
import easyapi
from flask_jwt import jwt_required, current_identity
import app.core as controller

token_bp = Blueprint(name='tokens', import_name='tokens', url_prefix='')


# 登录接口已存在 为 ： ‘/login’
# @admin_bp.route('/admins/login',methods=['GET','POST'])  #不写,methods=['GET','POST'] 默认是get
# def video_upload():
#     try:
#         pass
#     except easyapi.BusinessError as e:
#         return jsonify(**{
#             'msg': e.err_info,
#             'code': e.code,
#         }), e.http_code
#     return jsonify(code=200, msg='登录成功')

# 用户登录接口已由flask-jwt默认定义好，默认路由是"/auth"，可以在配置文件中配置:
# JWT_AUTH_URL_RULE = '/login'
# 修改登录接口路由为'/login'
# 需要注意的是，登录接口的传值要使用 application/json 形式


# @token_bp.route('/logout', methods=['GET'])
# def refresh_token():
#     return jsonify({ "msg": "安全退出成功", 'code': 200}), 200



@token_bp.route('/tokens', methods=['GET'])
@jwt_required()
def refresh_token():
    if current_identity is not None:
        try:
            token = controller.new_token(current_identity)
        except Exception as e:
            raise easyapi.BusinessError(code=500, http_code=200, err_info=str(e))
        return jsonify({"token": token.decode('utf-8'), "msg": "", 'code': 200}), 200
    raise easyapi.BusinessError(code=500, http_code=200, err_info="请先登录")


@token_bp.route('/current_user', methods=['GET'])
@jwt_required()
def get_current_user():
    if current_identity is not None:
        current_user = dict(current_identity)
        return jsonify({'current_user': current_user, 'msg': '','code': 200}), 200
    raise easyapi.BusinessError(code=500, http_code=200, err_info="请先登录")