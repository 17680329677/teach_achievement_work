from flask import jsonify, request
from app.api_1_0.sadmin import sadmin
from app.models import Teacher
from app import db
from werkzeug.security import generate_password_hash

'''
    校级管理员 super admin 密码修改
'''

'''
    修改密码  提交teacher_number 和新密码
    7180278 旧密码 123456 哈希：pbkdf2:sha256:50000$FQcWDDIY$812f7ba1b89fdb45879523653476b9678d4e83445e558501b731c635280a3354

'''
@sadmin.route('/password/update',methods=['GET','POST'])
def passwordCheck():
    teacherNumber = request.json['number']
    if teacherNumber is not None:
        teacher = Teacher.query.filter_by(number = teacherNumber).first()
        if teacher.verify_password(request.json['oldPasword']) :
            teacher.password = generate_password_hash(request.json['newPassword'])
            db.session.commit()
            #修改密码成功
            return jsonify({
                'code': 20000,
                'status': 'success'
            })
        else:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '原始密码错误'
            })

    else:
        return jsonify({
            'code':20001,
            'status':'failed',
            'reason':'未登录，或登陆超时'
        })

