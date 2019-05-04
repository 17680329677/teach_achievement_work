from flask import jsonify, request, current_app, json
from app.api_1_0 import api
from app.models import Teacher, TeacherType, TeacherInfo, Student
from app import db
from werkzeug.security import generate_password_hash

'''
    1.教师登陆，教师目前一共有5种角色（role）：
        校级管理员          sadmin  “super admin”                [开发]
        教务秘书(院级管理员) cadmin  “college admin”              [开发]
        科研院长            research_dean                           [未计划]
        教研室（系）主任     department_director                     [未计划]
        教师                normal  “normal user is teacher~”    [开发]
    
    2.学生登录，学生目前只有1种角色（role）：
        学生用户            student                              [开发]
'''
@api.route('/login/index', methods=['GET', 'POST'])
def login():
    username = request.json['username']
    password = request.json['password']
    type = request.json['type']  #用户类别

    if type == 'teacher':
        teacher = Teacher.query.filter_by(number = username).first()
        if teacher is not None and teacher.verify_password(password):
            teachers = {
                'code': 20000,
                'data': {
                    'token': teacher.number,
                    'type': 'teacher'
                }
            }
            return jsonify(teachers)
        else:
            teachers = {
                        'code': 20001,
                        'message': '用户名或密码错误！'
                    }
            return jsonify(teachers)
    elif type == 'student':
        student = Student.query.filter_by(id = username).first()
        if student is not None and student.password == password: #student.verify_password(password)
            return jsonify({
                'code': 20000,
                'status': 'success',
                'data': {
                    'token': student.id,
                    'type': 'student'
                }
            })
        else:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'message': '用户名或密码错误！',
                'reason': '用户名或密码错误！'
            })

'''
    根据token，获得用户详细信息

    return：
        'roles': （如果是学生：["student"]，返回值固定）
        'name':  用户姓名（学生暂时没有姓名字段，用学号代替吧）
        'number': 用户教师工号或学号
        'avatar': 用户头像 哈哈哈
        'type': teacher/student
'''
@api.route('/login/getinfo', methods=['GET', 'POST'])
def getInfo():
    token = request.json['token']
    userType = request.json['type']

    if userType == 'teacher':
        teacher = Teacher.query.filter_by(number = token).first() #获得教师用户角色代码
        if teacher is not None:
            # 获得用户角色字符 （sadmin，cadmin，research_dean，department_director，normal）
            #              校级管理员(系统管理员)，教务秘书(学院管理员)，科研院长，教研室系主任，教师
            role = TeacherType.query.filter_by(id=teacher.type).first().role
            #教师详细信息获得
            teacher_info = TeacherInfo.query.filter_by(number=request.json['token']).first()
            if teacher_info is not None:
                return jsonify({
                    'code': 20000,
                    'data': {
                        'roles': [role], #3月提问：为什么要打数组？？？一个教师账号不可能有多个角色，按照数据库设计？？   4.27回答：因为research_dean、department_director角色可以有多个权限。
                        'name': teacher_info.name,
                        'number': teacher_info.number,
                        'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',  #教师头像 哈哈哈
                        'type': 'teacher'
                    }
                })
            else:
                return jsonify({
                    'code': 20000,
                    'data': {
                        'roles': [role],
                        'name': "教师详细信息还没有补充完整，暂时没有姓名",
                        'number': teacher.number,
                        'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',  # 教师头像 哈哈哈
                        'type': 'teacher'
                    }
                })
        else:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '此账户未注册'
            })
    elif userType == 'student':
        student = Student.query.filter_by(id = token).first()
        if student is not None:
            return jsonify({
                'code': 20000,
                'data': {
                    'roles': ["student"],
                    'name': student.id,
                    'number': student.id,
                    'avatar': 'https://wpimg.wallstcn.com/f778738c-e4f8-4870-b634-56703b4acafe.gif',  #头像 哈哈哈
                    'type': 'student'
                }
            })
        else:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '此账户未注册'
            })

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


