from flask import jsonify, request, json
from app.api_1_0.sadmin import sadmin
from app.models import ProjectChildType,ProjectType
from app import db
from sqlalchemy import or_
from JSONHelper import JSONHelper

'''
    教师项目子类型
'''


'''
    信息展示
'''
@sadmin.route('/project_child_type/get', methods=['GET', 'POST'])
def getProjectChildType():
    projectChildTypes = db.session.query(ProjectChildType.id, ProjectChildType.child_type_name, ProjectChildType.parent_type_id,ProjectType.type_name)\
        .join(ProjectType, ProjectChildType.parent_type_id == ProjectType.id )\
        .all()
    projectChildType = JSONHelper.jsonBQlist(projectChildTypes)
    data = {
        'code': 20000,
        'status': 'success',
        'data': projectChildType
    }
    return jsonify(data)



'''
    添加
'''
@sadmin.route('/project_child_type/add', methods=['GET', 'POST'])
def addProjectChildType():
    parentTypeId = ProjectType.query.filter_by(id=request.json['parent_type_id'])
    if parentTypeId:
        projectChildType = ProjectChildType()
        projectChildType.child_type_name = request.json['child_type_name']
        projectChildType.parent_type_id = request.json['parent_type_id']
        db.session.add(projectChildType)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '添加成功'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有此项目父类型,无法添加'
        })

'''
    删除
'''
@sadmin.route('/project_child_type/del', methods=['GET', 'POST'])
def delProjectChildType():
    projectChildType = ProjectChildType.query.filter_by(id=request.json['id']).first()
    if projectChildType is not None:
        db.session.delete(projectChildType)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'failed'
        })


'''
    更新
'''
@sadmin.route('/project_child_type/update', methods=['GET', 'POST'])
def updateProjectChildType():
    projectChildType = ProjectChildType.query.filter_by(id=request.json['id']).first()
    if projectChildType is not None:
        parentTypeId = ProjectType.query.filter_by(id=request.json['parent_type_id'])
        if parentTypeId:
            projectChildType.child_type_name = request.json['child_type_name']
            projectChildType.parent_type_id = request.json['parent_type_id']
            db.session.commit()
            return jsonify({
                'code': 20000,
                'status': 'success',
                'reason': '更新成功'
            })
        else:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '没有此项目父类型，无法更新'
            })
    else:
        return jsonify({
            'code': 20000,
            'status': 'failed',
            'reason': 'can not find the selected college!'
        })



