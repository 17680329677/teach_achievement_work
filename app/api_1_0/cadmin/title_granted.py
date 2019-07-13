from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json
from werkzeug.security import generate_password_hash

from app import db
from app.models import Department,TeacherInfo,TitleRecord
from JSONHelper import JSONHelper

'''
    教师职称的授予、授予记录管理 相关工作
'''

'''
    显示所有职称授予记录 Log
'''
@cadmin.route('/title_granted/get',methods=['GET','POST'])
def getTitleGranted():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    

    #查询本院教师职称授予记录
    records = db.session.query(TitleRecord.id, TitleRecord.datetime,\
                               TitleRecord.teacher_number, TeacherInfo.name ,TitleRecord.teacher_title_id, TitleRecord.manager_title_id)\
    .join(TeacherInfo,TeacherInfo.number == TitleRecord.teacher_number).filter(  TeacherInfo.college_id == collegeId )\
            .order_by(TitleRecord.datetime.desc()).all()

    records = JSONHelper.jsonBQlist(records)

    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': records
    })

'''
    授予教师职称
'''
@cadmin.route('/teacher_title/grant',methods=['GET','POST'])
def grantTeacherGrant():
    number =  request.json['number']
    titleType =  request.json['title_type']
    titleId =  request.json['title_id']
    dateTime = request.json['datetime']

    titleGrant = TitleRecord()
    titleGrant.datetime = dateTime
    titleGrant.teacher_number = number
    if titleType == 'teach':
        titleGrant.teacher_title_id = titleId
        titleGrant.manager_title_id = None
    elif titleType == 'manage':
        titleGrant.teacher_title_id = None
        titleGrant.manager_title_id = titleId
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '未选择教师职称类型'
        })

    db.session.add(titleGrant)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '添加成功'
    })

"""
    导入教师职称
"""
@cadmin.route('/teacher_title/import',methods=['GET','POST'])
def importTeacherTitle():
    teacherName = request.get_data()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': ''
    })