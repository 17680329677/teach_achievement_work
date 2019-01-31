from flask import jsonify, request, json
from .. import api
from ...models import College, TeacherInfo
from app import db
from sqlalchemy import or_, and_
from JSONHelper import JSONHelper


@api.route('/secretary/index', methods=['GET', 'POST'])
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
            'code': 20000,
            'status': 'failed',
            'reason': 'something was wrong!'
        })


"""
    撤销指定教师的教务秘书职位
"""


@api.route('/secretary/recall', methods=['GET', 'POST'])
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
            'code': 20000,
            'status': 'failed',
            'reason': 'can not find the selected teacher or update wrong!'
        })


@api.route('/secretary/update', methods=['GET', 'POST'])
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


@api.route('/secretary/search', methods=['GET', 'POST'])
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

