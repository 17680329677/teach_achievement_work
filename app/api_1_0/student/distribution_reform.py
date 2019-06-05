from flask import jsonify, request
from app.api_1_0.student import student
from app import db

#from werkzeug.security import generate_password_hash
from JSONHelper import JSONHelper
from app.models import Student,DistributionResult,DistributionInfo,ClassInfo,College,DistributionDesire
import time
'''
    学生 student
'''

'''
    获取学生信息
'''
@student.route('/student_info/get',methods=['GET','POST'])
def getStudentInfo():
    studentId = request.json['token']  # token 是学号
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
    #print(gpaList)
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


'''
    获取学生志愿
'''
@student.route('/distribution_desire/get',methods=['GET','POST'])
def getDistributionDesire():
    studentId = request.json['token']  # token 是学号
    student  = Student.query.filter_by(id = studentId).first()
    collegeId = student.college_id

    desire = DistributionDesire.query.filter(DistributionDesire.student_id == studentId).order_by( DistributionDesire.desire_rank.asc() ).all()

    if desire:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': DistributionDesire.to_json(desire)
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': []
        })

'''
    添加志愿
'''
@student.route('/distribution_desire/add',methods=['GET','POST'])
def addDistributionDesire():
    studentId = request.json['token']  # token 是学号
    student  = Student.query.filter_by(id = studentId).first()
    collegeId = student.college_id

    #查询志愿是否存在
    existDesire = DistributionDesire.query.\
        filter( DistributionDesire.student_id == studentId,DistributionDesire.distribution_id == request.json['distribution_id'] )\
        .first()
    if existDesire:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '志愿已存在'
        })

    #查询志愿是否填满
    #full = DistributionDesire.query


    desire = DistributionDesire()
    desire.college_id = collegeId
    desire.student_id = studentId
    desire.distribution_id = request.json['distribution_id']
    desire.desire_rank = request.json['desire_rank']
    desire.submit_time = int(time.time())
    desire.status = '1'
    db.session.add(desire)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '提交成功'
    })