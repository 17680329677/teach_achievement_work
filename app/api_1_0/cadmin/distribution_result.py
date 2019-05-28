from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json

from JSONHelper import JSONHelper
from app import db
from app.models import Student,DistributionResult,DistributionInfo,TeacherInfo

'''
    ----------------------------分流结果-------------------------
'''

'''
    显示所有分流志愿  
'''
@cadmin.route('/distribution_result/get',methods=['GET','POST'])
def getDistributionResult():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    result = db.session.query(DistributionResult.id.label('id'),\
                              DistributionResult.student_id.label('student_id'),\
                              Student.name.label('student_name'),\
                              DistributionInfo.orientation_name.label('orientation_name'),\
                              DistributionResult.status.label('status') )\
        .join(Student, Student.id == DistributionResult.student_id) \
        .join(DistributionInfo, DistributionInfo.id == DistributionResult.distribution_id) \
        .filter(DistributionResult.college_id == collegeId).all()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': JSONHelper.jsonBQlist(result)
    })



'''
    按学号或学号查找学生信息
'''
@cadmin.route('/distribution_result/search', methods=['GET', 'POST'])
def searchDistributionResult():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    search_type = request.json['search_type']
    search_value = request.json['search_value']

    result = db.session.query(DistributionResult.id.label('id'),\
                              DistributionResult.student_id.label('student_id'),\
                              Student.name.label('student_name'),\
                              DistributionInfo.orientation_name.label('orientation_name'),\
                              DistributionResult.status.label('status') )\
        .join(Student, Student.id == DistributionResult.student_id) \
        .join(DistributionInfo, DistributionInfo.id == DistributionResult.distribution_id)

    if search_type == '' and search_value == '':
        result = result.filter(DistributionResult.college_id == collegeId).all()

    elif search_type == 'student_id':
        result = result.filter(DistributionResult.college_id == collegeId, Student.id.like('%' + search_value + '%')  ).all()
    elif search_type == 'student_name':
        result = result.filter(DistributionResult.college_id == collegeId, Student.name.like('%' + search_value + '%')  ).all()
    elif search_type == '' and search_value != '':
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '请选择查找类型'
        })

    if result:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(result)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有匹配的信息!'
        })

'''
    按是否确认状态 查询学生信息
'''
@cadmin.route('/distribution_result/search_status', methods=['GET', 'POST'])
def searchStatusDistributionResult():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    search_type = request.json['status']

    result = db.session.query(DistributionResult.id.label('id'),\
                              DistributionResult.student_id.label('student_id'),\
                              Student.name.label('student_name'),\
                              DistributionInfo.orientation_name.label('orientation_name'),\
                              DistributionResult.status.label('status') )\
        .join(Student, Student.id == DistributionResult.student_id) \
        .join(DistributionInfo, DistributionInfo.id == DistributionResult.distribution_id)\
        .filter(DistributionResult.college_id == collegeId, DistributionResult.status == search_type  ).all()

    if result:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(result)
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '学生已全部确认完毕!'
        })