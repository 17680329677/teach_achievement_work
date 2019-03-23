from flask import jsonify, request
from app.api_1_0.sadmin import sadmin
from app.models import TeacherType
from app import db

'''
    获取教师类型配置信息
'''
@sadmin.route('/teacher_type/get',methods=['GET','POST'])
def getAllTeacherType():
    teacherTypes = TeacherType.query.all()
    teacherType = TeacherType.to_json(teacherTypes)

    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': teacherType
    })


'''
    修改教师类型配置  只能修改 type_name 
'''
@sadmin.route('/teacher_type/update',methods=['GET','POST'])
def updateTeacherType():
    id = request.json['id']
    if id is not None:
        teacherType = TeacherType.query.filter_by(id = id).first()
        if teacherType is not None:
            teacherType.type_name = request.json['type_name']
            db.session.commit()
            return jsonify({
                'code': 20000,
                'status': 'success'
            })
        else:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '没有此教师类型'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '教师类型id为空'
        })
