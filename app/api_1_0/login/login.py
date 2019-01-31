from flask import jsonify, request, current_app, json
from .. import api
from ...models import Teacher, Teacher_Type, TeacherInfo
from app import db
from werkzeug.security import generate_password_hash


@api.route('/login/teachers', methods=['GET', 'POST'])
def teacher_login():
    print(request.json['type'])
    if request.json['type'] == 'teacher':
        teacher = Teacher.query.filter_by(number=request.json['username']).first()
        print(teacher)
        if teacher is not None and teacher.verify_password(request.json['password']):
            teachers = {
                'code': 20000,
                'data': {
                    'token': teacher.number
                }
            }
            return jsonify(teachers)
        else:
            teachers = {
                        'code': 20001,
                        'message': '用户名或密码错误！'
                    }
            return jsonify(teachers)


@api.route('/login/getinfo', methods=['GET', 'POST'])
def getInfo():
    teacher = Teacher.query.filter_by(number=request.json['token']).first()
    if teacher is not None:
        role = Teacher_Type.query.filter_by(id=teacher.type).first().role
        teacher_info = TeacherInfo.query.filter_by(number=request.json['token']).first()
        if teacher_info is not None:
            data = {
                'code': 20000,
                'data': {
                    'roles': [role],
                    'name': teacher_info.name,
                    'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'
                }
            }
        else:
            data = {
                'code': 20001,
                'status': 'failed',
                'reason': 'Do not have this account!'
            }
    return jsonify(data)


@api.route('/login/logout', methods=['GET', 'POST'])
def logout():
    res = {
        'code': 20000,
        'data': 'success'
    }
    return jsonify(res)


@api.route('/dev/password', methods=['GET', 'POST'])
def pwd_hash():
    teachers = Teacher.query.all()
    for teacher in teachers:
        teacher.password = generate_password_hash(teacher.password)
        db.session.commit()
    return 'success'


