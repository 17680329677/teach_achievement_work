from flask import jsonify, request
from app.api_1_0.student import student
from app import db

#from werkzeug.security import generate_password_hash
from JSONHelper import JSONHelper
from app.models import Student,DistributionResult,DistributionInfo

'''
    学生 student
'''


'''
    显示分流结果
'''
@student.route('/distribution_result/get',methods=['GET','POST'])
def getDistributionResult():
    studentId = request.json['token']  # token 是学号

    result = db.session.query(DistributionResult.id.label('id'),\
                              DistributionResult.student_id.label('student_id'),\
                              Student.name.label('student_name'),\
                              DistributionInfo.orientation_name.label('orientation_name'),\
                              DistributionResult.status.label('status') )\
        .join(Student, Student.id == DistributionResult.student_id) \
        .join(DistributionInfo, DistributionInfo.id == DistributionResult.distribution_id) \
        .filter(DistributionResult.student_id == studentId).first()

    if result:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQfirst(result)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '未查询到信息'
        })

@student.route('/distribution_result/confirm',methods=['GET','POST'])
def confirmDistributionResult():
    studentId = request.json['token']  # token 是学号

    student = Student.query.filter_by(id=studentId).first()

    if request.json['password'] == request.json['repassword']:
        if student.password == request.json['password']:
            distributionResult = DistributionResult.query.filter_by(student_id = studentId).first()
            if distributionResult:
                distributionResult.status = '1'
                db.session.commit()
                return jsonify({
                    'code': 20000,
                    'status': 'success',
                    'reason': '确认成功'
                })
            else:
                return jsonify({
                    'code': 20001,
                    'status': 'failed',
                    'reason': '未查询到分流结果'
                })
        else:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '密码错误'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '重复密码不一致'
        })




