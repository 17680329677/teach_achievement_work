from flask import jsonify, request, json
from app.api_1_0.sadmin import sadmin
from app.models import ProjectType
from app import db
from sqlalchemy import or_

'''
    教师项目父类型配置操作
'''

'''
    信息展示
'''
@sadmin.route('/project_type/get', methods=['GET', 'POST'])
def getAllProjectType():
    projectTypes = ProjectType.query.all()
    projectType = ProjectType.to_json(projectTypes)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': projectType
    })

'''
    信息添加
'''
@sadmin.route('/project_type/add', methods=['GET', 'POST'])
def addProjectType():
    if request.json['type_name'] and  request.json['student_attend']:
        projectType = ProjectType()
        projectType.type_name = request.json['type_name']
        projectType.student_attend = request.json['student_attend']
        try:
            db.session.add(projectType)
            db.session.commit()
            return jsonify({
                'code':20000,
                'status': 'success'
            })
        except:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '保存失败！'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '信息不完整'
        })


'''
    信息删除
'''
@sadmin.route('/project_type/del', methods=['GET', 'POST'])
def delProjectType():
    projectType = ProjectType.query.filter_by(id=request.json['id']).first()
    if projectType is not None:
        db.session.delete(projectType)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有此项目类型id'
        })


'''
    信息更新
'''
@sadmin.route('/project_type/update', methods=['GET', 'POST'])
def updateProjectType():
    projectType = ProjectType.query.filter_by(id=request.json['id']).first()
    if projectType is not None:
        projectType.type_name = request.json['type_name']
        projectType.student_attend = request.json['student_attend']
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '信息更新成功'
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'failed',
            'reason': '未查询到此项目信息，更新失败'
        })
