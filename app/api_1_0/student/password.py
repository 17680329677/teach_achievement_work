from flask import jsonify, request
from app.api_1_0.student import student
from app import db

#from werkzeug.security import generate_password_hash
from app.models import Student

'''
    学生 student
'''

'''
    修改密码
    params: token:id
            oldPasword:
            newPassword:
'''
@student.route('/password/update',methods=['GET','POST'])
def passwordChange():
    token = request.json['token']
    if token is not None:
        student = Student.query.filter_by(id = token).first()
        if student.password == request.json['oldPasword'] :
            student.password = request.json['newPassword']  #generate_password_hash(request.json['newPassword'])
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
