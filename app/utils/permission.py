from flask import jsonify
from flask_jwt import jwt_required, current_identity

from easyapi.permission import AbcPermission


class MyPermission(AbcPermission):

    @classmethod
    def check(cls, *args, **kwargs):
        if current_identity is not None and current_identity.get('type', 'default') in args:
            return True
        else:
            return False

    @classmethod
    def fail(cls):
        return jsonify(code=403, msg="权限不足"), 404
