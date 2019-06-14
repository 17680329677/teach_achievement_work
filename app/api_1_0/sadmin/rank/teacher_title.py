from flask import jsonify, request
from app.api_1_0.sadmin import sadmin
from app.models import TeacherTitle,TeacherType,TeacherCategory
from app import db
from JSONHelper import JSONHelper

'''
    教师职称配置
'''

'''
    所有教师职称信息
'''
@sadmin.route('/teacher_title/get',methods=['GET','POST'])
def getAllTeacherTitleInfo():
    teacherTitles = db.session.query(TeacherTitle.id,TeacherTitle.name,TeacherCategory.name.label('teacher_category_name'))\
        .join(TeacherCategory, TeacherCategory.id == TeacherTitle.teacher_category_id)\
        .all()
    teacherTitle = JSONHelper.jsonBQlist(teacherTitles)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': teacherTitle
    })

'''
    增加教师职称
'''
@sadmin.route('/teacher_title/add',methods=['GET','POST'])
def addTeacherTitle():
    name = request.json['name']
    teacher_category_id = request.json['teacher_category_id']

    teacherTitle = TeacherTitle()
    teacherTitle.name = name
    teacherTitle.teacher_category_id = teacher_category_id
    db.session.add(teacherTitle)
    db.session.commit()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '添加成功'
    })


'''
    删除职称配置信息
'''
@sadmin.route('/teacher_title/del',methods=['GET','POST'])
def delTeacherTitle():
    titleId = request.json['id']
    if titleId is not None:
        teacherTitle = TeacherTitle.query.filter_by(id = titleId).first()
        db.session.delete(teacherTitle)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有要删除的职称id'
        })

'''
    更新教师职称信息
'''
@sadmin.route('/teacher_title/update',methods=['GET','POST'])
def updateTeacherTitle():
    titleId = request.json['id']
    titleName = request.json['name']
    typeId = request.json['type_id']
    if titleId is not None and titleName is not None and typeId is not None:
        teacherTitle = TeacherTitle.query.filter_by(id = titleId).first()
        teacherTitle.name = titleName
        teacherTitle.type_id = typeId
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有职称id、名称、教师类型'
        })