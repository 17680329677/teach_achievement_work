from flask import jsonify, request, json
from app.api_1_0.sadmin import sadmin
from app.models import College, TeacherInfo,Teacher
from app import db
from sqlalchemy import or_, and_
from JSONHelper import JSONHelper

'''
    当前已有的院级管理员(教务秘书)信息展示  TeacherInfo.type_id == 2
'''
@sadmin.route('/secretary/index', methods=['GET', 'POST'])
def getAllSecretaryInfo():
    secretary = db.session.query(TeacherInfo.id.label('id'), College.name.label('college_name'),
                                 College.college_id.label('college_id'), TeacherInfo.name.label('secretary_name'),
                                 TeacherInfo.telephone.label('phone'), TeacherInfo.email.label('email'),
                                 TeacherInfo.number.label('number'))\
                          .join(College, TeacherInfo.college_id == College.id)\
                          .filter(TeacherInfo.type_id == 2).all()
    # print(JSONHelper.jsonBQlist(secretary))
    if secretary is not None:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(secretary)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'something was wrong!'
        })

'''
    增加院级管理员 by Teacher.number
'''
@sadmin.route('/secretary/add', methods=['GET', 'POST'])
def addSecretary():
    teacher = Teacher.query.filter_by(number = request.json['number']).first()
    if teacher is not None:
        if teacher.type == 2:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': 'the secretary teacher has already existed'
            })
        else:
            # 修改Teacher表的type：
            teacher.type = 2
            db.session.commit()
            # 修改teacher_info表的type_id
            teacherInfo = TeacherInfo.query.filter_by(number = request.json['number']).first()
            if teacherInfo is not None:
                teacherInfo.type_id = 2
                db.session.commit()
            return jsonify({
                'code': 20000,
                'status': 'success'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'the teacher account is not exist,please registe a teacher account'
        })

'''
    【更改】撤销指定教师的教务秘书职位 by TeacherInfo.id  把教师是院级管理员的身份改为普通教师
'''
@sadmin.route('/secretary/recall', methods=['GET', 'POST'])
def recallSecretary():
    secretary = TeacherInfo.query.filter_by(id=request.json['id']).first()
    if secretary is not None:
        secretary.type_id = 5
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'can not find the selected teacher or update wrong!'
        })

'''
    更改 院级管理员的 电话 mail信息 by TeacherInfo.number
'''
@sadmin.route('/secretary/update', methods=['GET', 'POST'])
def updateSecretary():
    teacher = TeacherInfo.query.filter_by(number=request.json['number']).first()
    if teacher is not None and teacher.type_id == 2:
        teacher.telephone = request.json['telephone']
        teacher.email = request.json['email']
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'failed',
            'reason': 'teacher was not found or is not a secretary!'
        })

'''
    【查询】学院管理员详细信息查询 by 院级管理员名字 或者 学院名称 模糊查询
'''
@sadmin.route('/secretary/search', methods=['GET', 'POST'])
def searchSecretary():
    search_type = request.json['search_type']
    search_value = request.json['search_value']
    if search_type == '' and search_value == '':
        secretary = db.session.query(TeacherInfo.id.label('id'), College.name.label('college_name'),
                                     College.college_id.label('college_id'), TeacherInfo.name.label('secretary_name'),
                                     TeacherInfo.telephone.label('phone'), TeacherInfo.email.label('email'),
                                     TeacherInfo.number.label('number')) \
            .join(College, TeacherInfo.college_id == College.id) \
            .filter(TeacherInfo.type_id == 2).all()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(secretary)
        })
    elif search_type == 'secretary_name':
        secretary = db.session.query(TeacherInfo.id.label('id'), College.name.label('college_name'),
                                     College.college_id.label('college_id'), TeacherInfo.name.label('secretary_name'),
                                     TeacherInfo.telephone.label('phone'), TeacherInfo.email.label('email'),
                                     TeacherInfo.number.label('number')) \
            .join(College, TeacherInfo.college_id == College.id) \
            .filter(and_(TeacherInfo.type_id==2, TeacherInfo.name.like('%' + search_value + '%'))).all()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(secretary)
        })
    elif search_type == 'college_name':
        secretary = db.session.query(TeacherInfo.id.label('id'), College.name.label('college_name'),
                                     College.college_id.label('college_id'), TeacherInfo.name.label('secretary_name'),
                                     TeacherInfo.telephone.label('phone'), TeacherInfo.email.label('email'),
                                     TeacherInfo.number.label('number')) \
            .join(College, TeacherInfo.college_id == College.id) \
            .filter(and_(TeacherInfo.type_id == 2, College.name.like('%' + search_value + '%'))).all()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(secretary)
        })
    elif search_type == '' and search_value != '':
        return jsonify({
            'code': 20000,
            'status': 'failed',
            'reason': 'please selected search type!'
        })

