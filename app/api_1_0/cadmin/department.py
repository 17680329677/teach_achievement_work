from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json

from app import db
from app.models import Department,TeacherInfo

'''
    教研室信息表
'''

#  --------------------------------------有各种信息的显示--------------------------------------
'''
    显示教研室 主体信息
'''
@cadmin.route('/department/get',methods=['GET','POST'])
def getAllDepartment():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    #显示所有教研室的时候 将number字段更新  number = TeacherInfo.query.filter_by(department_id = departmentId).count()

    departments = Department.query.filter_by(college_id = collegeId).all()
    for department in departments:
        department.number = TeacherInfo.query.filter_by(department_id = department.id).count()
    db.session.commit()

    department = Department.to_json(departments)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': department
    })

'''
    计算某个教研室的人数 
    暂时不用 直接使用department中的number字段
'''
@cadmin.route('/department/get_number',methods=['GET','POST'])
def getDaprtmentNumber():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    departmentId = request.json['id']
    number = TeacherInfo.query.filter_by(department_id = departmentId).count()
    if number is not None:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': {
                'number':number
            }
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': {
                'number':None
            }
        })

#  --------------------------------------教师添加进教研室的流程--------------------------------------
#（关教研室信息的操作也需要用到）
'''
    检查教师是否分配教研室
    教研室id不存在 或 id=0 都算是未分配教研室，(假设有可能有废弃教研室id 一般删除教研室的时候，该教研室所有教师department_id=0)
    不存在： return 0
    存在： return "教研室名称"
'''
def checkJoinDepartment(teacherNumber):
    departmentId = None
    teacherInfo = TeacherInfo.query.filter_by(number = teacherNumber).first()
    if teacherInfo:
        departmentId = teacherInfo.department_id
    department = Department.query.filter_by(id = departmentId).first()
    if departmentId == 0 or departmentId is None:
        return 0
    elif not department:
        #查询是否为废弃教研室id
        return 0
    else:
        return department.name

'''
    将教师添加到教研室（也包括教研室主任）   同步修改TeacherInfo中的department_id值
    return 1 添加成功
    return 0 未发现此教师
'''
def addTeacherInfoToDepartment(teacherNumber,departmentId):
    teacherInfo = TeacherInfo.query.filter_by(number=teacherNumber).first()
    if teacherInfo is not None:
        teacherInfo.department_id = departmentId
        db.session.commit()
        return 1
    else:
        return 0


#  --------------------------------------有关教研室信息的操作--------------------------------------
'''
    新增教研室
'''
@cadmin.route('/department/add',methods=['GET','POST'])
def addDpartment():
    name = request.json['name'] #教研室名称
    directorNumber = request.json['director'] #顺便添加教研室主任

    cadminToken = request.json['token'] #token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number = cadminToken).first()
    collegeId = cadminInfo.college_id

    #检查主任是否分配教研室
    departmentName = checkJoinDepartment(directorNumber)
    if departmentName:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': "已被添加到："+departmentName
        })


    #如果主任未添加到教研室，新增教研室信息
    department = Department()
    department.name = name
    department.director = directorNumber
    department.college_id = collegeId
    department.number = 0 #教研室人数初始化为0  在更新页面的时候重新计算

    try:
        db.session.add(department)
        db.session.commit()

        # 将主任教师添加到教研室
        res = addTeacherInfoToDepartment(directorNumber,department.id)
        if res == 1:
            return jsonify({
                'code': 20000,
                'status': 'success',
                'reason': '添加成功'
            })
        elif res == 0:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '未发现此教师'
            })
        else:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '未知错误 res：' + res
            })
    except:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '保存失败！'
        })

'''
    删除教研室
'''
@cadmin.route('/department/del',methods=['GET','POST'])
def delDepartment():
    departmentId = request.json['id']
    #将属于本教研室的所有教师教研室id改为0
    teacherInfos = TeacherInfo.query.filter_by(department_id = departmentId).all()
    for teacherInfo in teacherInfos:
        teacherInfo.department_id = 0
    db.session.commit()
    #删除教研室
    department = Department.query.filter_by(id = departmentId).first()
    db.session.delete(department)
    try:
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    except:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '删除失败！'
        })

'''
    修改教研室 （修改教研室名称、教研室主任）
'''
@cadmin.route('/department/update',methods=['GET','POST'])
def updateDepartment():
    id = request.json['id']
    name = request.json['name']
    director = request.json['director']

    department = Department.query.filter_by(id = id).first()
    department.name = name
    department.director = director
    try:
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    except:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '更新失败！'
        })




#  --------------------------------------有关教研室的成员操作--------------------------------------
'''
    新增教研室人员 添加教师
'''

@cadmin.route('/department/add_teacher', methods=['GET', 'POST'])
def departmentAddTeacher():
    teacherNumber = request.json['number']
    departmentId = request.json['department_id']
    teacherInfo = TeacherInfo.query.filter_by(number=teacherNumber).first()
    if teacherInfo is not None:
        check = checkJoinDepartment(teacherNumber)
        if check:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': "已被添加到：" + check
            })
        else:
            res = addTeacherInfoToDepartment(teacherNumber, departmentId)
            if res == 1:
                return jsonify({
                    'code': 20000,
                    'status': 'success',
                    'reason': '添加成功'
                })
            elif res == 0:
                return jsonify({
                    'code': 20001,
                    'status': 'failed',
                    'reason': '未发现此教师'
                })
            else:
                return jsonify({
                    'code': 20001,
                    'status': 'failed',
                    'reason': '未知错误 res：' + res
                })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有此教师详细信息'
        })



'''
    删除教研室人员
'''

@cadmin.route('/department/del_teacher', methods=['GET', 'POST'])
def departmentDeleteTeacher():
    teacherNumber = request.json['number']
    teacherInfo = TeacherInfo.query.filter_by(number=teacherNumber).first()
    if teacherInfo is not None:
        teacherInfo.department_id = 0

        # 如果是教研室主任 同步删除department中的director
        director = Department.query.filter_by(director=teacherNumber).first()
        if director:
            director.director = ''
        db.session.commit()

        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '删除成功'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有此教师详细信息'
        })
