from flask import jsonify, request
from app.api_1_0.student import student
from app import db

#from werkzeug.security import generate_password_hash
from app.models import Student,DistributionInfo

'''
    student optino
'''

'''
    选项信息获取
        1.学生所在学院分流方向获取
'''

'''
    1.学生所在学院分流方向获取
'''
@student.route('/distribution_options/get',methods=['GET','POST'])
def getDistributionOptions():
    studentId = request.json['token']  # token 是学号
    student = Student.query.filter_by(id=studentId).first()
    collegeId = student.college_id

    options = DistributionInfo.query.filter_by(college_id = collegeId).all()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': DistributionInfo.to_json(options)
    })