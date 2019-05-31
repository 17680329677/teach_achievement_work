from flask import jsonify, request
from app.api_1_0.student import student
from app import db

#from werkzeug.security import generate_password_hash
from JSONHelper import JSONHelper
from app.models import Student,DistributionResult,DistributionInfo,ClassInfo,College

'''
    学生 student
'''

'''
    获取学生信息
'''
@student.route('/student_info/get',methods=['GET','POST'])
def getStudentInfo():
    studentId = request.json['token']  # token 是管理员的工号
    student  = Student.query.filter_by(id = studentId).first()
    collegeId = student.college_id

    result = db.session.query(Student.id.label('id'),\
                              Student.name.label('name'),\
                              Student.gender.label('gender'),\
                              ClassInfo.class_name.label('class_name'),\
                              College.name.label('college_name'),\
                              Student.gpa.label('gpa') )\
        .join(ClassInfo, ClassInfo.id == Student.class_id)\
        .join(College, College.id == Student.college_id)\
        .filter(Student.id == studentId).first()

    jsondata = {}
    for i in range(result.__len__()):
        tdic = {result._fields[i]: str(result[i])}
        jsondata.update(tdic)

    result = jsondata

    #加入gpa排名
    gpaList = db.session.query(Student).filter(Student.college_id == collegeId).order_by(Student.gpa.desc()).all()
    gpaRank = 0;
    print(gpaList)
    for item in gpaList:
        gpaRank = gpaRank +1
        if item.id == int(studentId):
            break

    result['gpa_rank'] = gpaRank
    #加入学生数量
    result['student_quantity'] = Student.query.filter_by(college_id = collegeId).count()

    if result:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': result
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有查找到信息'
        })
