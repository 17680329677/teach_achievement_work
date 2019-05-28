from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json

from JSONHelper import JSONHelper
from app import db
from app.models import DistributionInfo,TeacherInfo

'''
    ----------------------------分流配置信息-------------------------
'''

'''
    显示所有分流配置信息
'''
@cadmin.route('/distribution_info/get',methods=['GET','POST'])
def getDistributionInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    distributionInfo = DistributionInfo.query.filter_by(college_id=collegeId).all()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': DistributionInfo.to_json(distributionInfo)
    })


'''
    添加配置信息
'''
@cadmin.route('/distribution_info/add',methods=['GET','POST'])
def addDistributionInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    distributionInfo = DistributionInfo()
    distributionInfo.college_id = collegeId
    distributionInfo.orientation_name = request.json['orientation_name']
    distributionInfo.num_limit = request.json['num_limit']
    distributionInfo.start_time = request.json['start_time']
    distributionInfo.end_time = request.json['end_time']

    db.session.add(distributionInfo)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '添加成功'
    })

'''
    修改配置信息
'''
@cadmin.route('/distribution_info/update',methods=['GET','POST'])
def updateDistributionInfo():
    id = request.json['id']

    distributionInfo = DistributionInfo.query.filter_by(id = id).first()
    distributionInfo.orientation_name = request.json['orientation_name']
    distributionInfo.num_limit = request.json['num_limit']
    distributionInfo.start_time = request.json['start_time']
    distributionInfo.end_time = request.json['end_time']
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '修改成功'
    })

'''
    删除配置信息
'''
@cadmin.route('/distribution_info/del',methods=['GET','POST'])
def delDistributionInfo():
    id = request.json['id']

    distributionInfo = DistributionInfo.query.filter_by(id = id).first()
    db.session.delete(distributionInfo)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '删除成功'
    })