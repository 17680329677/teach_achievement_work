from flask import jsonify, request, json
from app.api_1_0.normal import normal
from sqlalchemy import or_
import json
from werkzeug.security import generate_password_hash

from app import db
from app.models import Department,TeacherInfo,College,TeacherTitle,BookRank,ProjectRank,ProjectType,ProjectChildType,InnovationRank
from JSONHelper import JSONHelper

'''
    选项信息获取
        1.学院
        2.教研室
        3.教师职称
        4.学院教师信息【id+name+department_id】
        5.教研室教师信息【id+name+department_id】
        6.出版教材等级 BookRank
        7.教改项目等级 ProjectRank
        8.教改项目类型 ProjectType
        9.教改项目子类型 ProjectChildType  
        10.大创等级 InnovationRank
'''


'''
    1.挂载 学院选项
'''
@normal.route('/college_options/get',methods=['GET','POST'])
def getCollegeOptions():
    options = College.query.filter_by().all()
    if not options:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '选项信息为空'
        })
    option = College.to_json(options)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': option
    })


'''
    2.挂载 本学院教研室选项
'''
@normal.route('/department_options/get',methods=['GET','POST'])
def getDepartmentOptions():
    options = Department.query.filter_by().all()
    if not options:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '选项信息为空'
        })
    option = Department.to_json(options)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': option
    })


'''
    3.挂载 教师职称选项
'''
@normal.route('/teacher_title_option/get',methods=['GET','POST'])
def getAllTeacherTitleOption():
    teacherTitles = TeacherTitle.query.all()
    teacherTitleOption = TeacherTitle.to_json(teacherTitles)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': teacherTitleOption
    })


'''
    4.挂载 当前学院所有教师的 工号+姓名+所属教研室id  【by 管理员工号】
    :return   number  name  department_id
'''
@normal.route('/teacher_info_number_name/get',methods=['GET','POST'])
def getTeacherNumberAndNameInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    teacherInfos = db.session.query(TeacherInfo.number.label('number'),TeacherInfo.name.label('name'),TeacherInfo.department_id.label('department_id'))\
        .filter(TeacherInfo.college_id == collegeId).all()

    if teacherInfos is not None:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(teacherInfos)
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': ''
        })


'''
    5.挂载 本教研室的 所有教师的 工号+姓名+所属教研室id 【by 教研室id】
    :return   number  name  department_id
'''
@normal.route('/teacher_info_number_name/get_by_department_id',methods=['GET','POST'])
def getTeacherNumberAndNameByDepartmentId():
    departmentId = request.json['department_id']

    teacherInfos = db.session.query(TeacherInfo.number.label('number'),TeacherInfo.name.label('name'),TeacherInfo.name.label('department_id')  )\
        .filter(TeacherInfo.department_id == departmentId).all()

    if teacherInfos is not None:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(teacherInfos)
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': ''
        })

'''
    6.挂载 出版教材等级选项
'''
@normal.route('/book_rank_options/get',methods=['GET','POST'])
def getBookRankOptions():
    options = BookRank.query.all()
    if not options:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '选项信息为空'
        })
    option = BookRank.to_json(options)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': option
    })

'''
    7.教改项目等级 ProjectRank
'''
@normal.route('/project_rank_options/get',methods=['GET','POST'])
def getProjectRankOptions():
    options = ProjectRank.query.all()
    if not options:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '选项信息为空'
        })
    option = ProjectRank.to_json(options)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': option
    })

'''
    8.教改项目类型 ProjectType
'''
@normal.route('/project_type_options/get',methods=['GET','POST'])
def getProjectTypeOptions():
    options = ProjectRank.query.all()
    if not options:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '选项信息为空'
        })
    option = ProjectType.to_json(options)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': option
    })

'''
    9.教改项目子类型 ProjectChildType  
'''
@normal.route('/project_child_type_options/get',methods=['GET','POST'])
def getProjectChildTypeOptions():
    options = ProjectChildType.query.all()
    if not options:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '选项信息为空'
        })
    option = ProjectChildType.to_json(options)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': option
    })

'''
    10.大创等级 InnovationRank
'''
@normal.route('/innovation_rank_options/get',methods=['GET','POST'])
def getInnovationRankOptions():
    options = InnovationRank.query.all()
    if not options:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '选项信息为空'
        })
    option = InnovationRank.to_json(options)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': option
    })