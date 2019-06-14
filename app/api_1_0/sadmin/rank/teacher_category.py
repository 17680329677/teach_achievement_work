from flask import jsonify, request, json
from app.api_1_0.sadmin import sadmin
from app.models import TeacherCategory
from app import db
from sqlalchemy import or_

'''
   teacher_category 配置
'''

'''
    信息展示
'''
@sadmin.route('/teacher_category/get', methods=['GET', 'POST'])
def getTeacherCategory():
    teachercCategory = TeacherCategory.query.all()
    teachercCategory = TeacherCategory.to_json(teachercCategory)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': teachercCategory
    })

'''
    添加
'''
@sadmin.route('/teacher_category/add', methods=['GET', 'POST'])
def addTeacherCategory():
    if request.json['name']:
        teachercCategory = TeacherCategory()
        teachercCategory.name = request.json['name']
        try:
            db.session.add(teachercCategory)
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
    删除
'''
@sadmin.route('/teacher_category/del', methods=['GET', 'POST'])
def delTeacherCategory():
    teachercCategory = TeacherCategory.query.filter_by(id=request.json['id']).first()
    if teachercCategory is not None:
        db.session.delete(teachercCategory)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有此类型id'
        })


'''
    更新
'''
@sadmin.route('/teacher_category/update', methods=['GET', 'POST'])
def updateTeacherCategory():
    teachercCategory = TeacherCategory.query.filter_by(id=request.json['id']).first()
    if teachercCategory is not None:
        teachercCategory.name = request.json['name']
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
