from flask import jsonify, request, json
from app.api_1_0.sadmin import sadmin
from app.models import College, TeacherInfo
from app import db
from sqlalchemy import or_


@sadmin.route('/college/index', methods=['GET', 'POST'])
def getAllCollegeInfo():
    # colleges = db.session.query(College.id, College.name, College.college_id, TeacherInfo.name, TeacherInfo.telephone)\
    #                     .join(TeacherInfo, College.id == TeacherInfo.college_id)\
    #                     .filter(TeacherInfo.type_id == 2).order_by(College.id).all()
    # page_index = request.json['page_index']
    colleges = College.query.all()
    college = College.to_json(colleges)
    data = {
        'code': 20000,
        'status': 'success',
        'data': college
    }
    return jsonify(data)


@sadmin.route('/college/update', methods=['GET', 'POST'])
def collegeUpdate():
    college = College.query.filter_by(id=request.json['id']).first()
    if college is not None:
        college.name = request.json['college_name']
        college.college_id = request.json['college_id']
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': 'update success!'
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'failed',
            'reason': 'can not find the selected college!'
        })


@sadmin.route('/college/delete', methods=['GET', 'POST'])
def collegeDelete():
    college = College.query.filter_by(id=request.json['id']).first()
    if college is not None:
        db.session.delete(college)
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


@sadmin.route('/college/add', methods=['GET', 'POST'])
def collegeAdd():
    college = College.query.\
        filter(or_(College.college_id==request.json['college_id'], College.name==request.json['college_name'])).first()
    if college is not None:
        return jsonify({
            'code': 20000,
            'status': 'failed',
            'reason': 'college_id or name was duplicated！'
        })
    college = College()
    college.name = request.json['college_name']
    college.college_id = request.json['college_id']
    db.session.add(college)
    db.session.commit()
    return jsonify({
        'code': 20000,
        'status': 'success'
    })


