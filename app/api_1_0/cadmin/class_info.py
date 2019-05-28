from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json

from JSONHelper import JSONHelper
from app import db
from app.models import ClassInfo,TeacherInfo

'''
        班级信息
'''

'''
    查看当前学院所有班级
'''
@cadmin.route('/class_info/get',methods=['GET','POST'])
def getClassInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    classInfo = ClassInfo.query.filter_by(college_id=collegeId).all()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': ClassInfo.to_json(classInfo)
    })

'''
    添加班级
'''
@cadmin.route('/class_info/add',methods=['GET','POST'])
def addClassInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    classInfo = ClassInfo()
    classInfo.class_name = request.json['class_name']
    classInfo.college_id = collegeId
    classInfo.grade = request.json['grade']
    classInfo.status = request.json['status']

    db.session.add(classInfo)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '添加成功'
    })


'''
    删除班级
'''
@cadmin.route('/class_info/del',methods=['GET','POST'])
def delClassInfo():
    id = request.json['id']

    classInfo = ClassInfo.query.filter_by(id = id).first()
    db.session.delete(classInfo)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '删除成功'
    })