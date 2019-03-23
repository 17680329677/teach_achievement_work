from flask import jsonify, request, current_app, json
from app.api_1_0 import api
from app.models import Teacher, TeacherType, TeacherInfo
from app import db
from werkzeug.security import generate_password_hash

'''
教师登陆 教师目前一共有5种校色：

校级管理员          sadmin  “super admin”                [准备开发]
教务秘书(院级管理员) cadmin  “college admin”              [准备开发]
科研院长            research_dean               [未计划]
教研室（系）主任     department_director         [未计划]
教师                normal  “normal user is teacher~”    [准备开发]
'''
@api.route('/login/teachers', methods=['GET', 'POST'])
def teacher_login():
    print(request.json['type']) #教师类别
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

'''
根据token=teacher.number，获得教师信息：1.角色信息 2.
'''
@api.route('/login/getinfo', methods=['GET', 'POST'])
def getInfo():
    teacher = Teacher.query.filter_by(number=request.json['token']).first() #获得教师用户角色代码
    if teacher is not None:
        # 获得用户角色字符 （sadmin，cadmin，research_dean，department_director，normal）
        #              校级管理员(系统管理员)，教务秘书(学院管理员)，科研院长，教研室系主任，教师
        role = TeacherType.query.filter_by(id=teacher.type).first().role
        #教师详细信息获得
        teacher_info = TeacherInfo.query.filter_by(number=request.json['token']).first()
        if teacher_info is not None:
            data = {
                'code': 20000,
                'data': {
                    'roles': [role], #为什么要打数组？？？一个教师账号不可能有多个角色，按照数据库设计？？？
                    'name': teacher_info.name,
                    'number': teacher_info.number,
                    'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif'#教师头像 哈哈哈
                }
            }
        else:
            data = {
                'code': 20001,
                'status': 'failed',
                'reason': 'Do not have this account!'
            }
    return jsonify(data)

'''
教师用户推出登陆
'''
@api.route('/login/logout', methods=['GET', 'POST'])
def logout():
    res = {
        'code': 20000,
        'data': 'success'
    }
    return jsonify(res)

'''
当前教师用户密码全部哈希
'''
@api.route('/dev/password', methods=['GET', 'POST'])
def pwd_hash():
    teachers = Teacher.query.all()
    for teacher in teachers:
        teacher.password = generate_password_hash(teacher.password)
        db.session.commit()
    return 'success'


