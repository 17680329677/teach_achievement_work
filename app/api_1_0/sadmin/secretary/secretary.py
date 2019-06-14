from flask import jsonify, request, json
from app.api_1_0.sadmin import sadmin
from app.models import College, TeacherInfo,Teacher
from app import db
from sqlalchemy import or_, and_
from JSONHelper import JSONHelper
from werkzeug.security import generate_password_hash

'''
    当前已有的院级管理员(教务秘书)信息展示  TeacherInfo.type_id == 2
'''
@sadmin.route('/secretary/index', methods=['GET', 'POST'])
def getAllSecretaryInfo():
    secretary = db.session.query( TeacherInfo.number, College.name.label('college_name')  )\
                          .join(College, TeacherInfo.college_id == College.id)\
                          .filter(TeacherInfo.type_id == 2).order_by( TeacherInfo.college_id.asc() ).all()
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
    增加院级管理员 创建账号
'''
@sadmin.route('/secretary/add', methods=['GET', 'POST'])
def addSecretary():
    number = request.json['number']
    password = generate_password_hash( '123456' ) #初始化密码默认为 123456
    type = 2 #学院管理员权限等级是2

    college_id = request.json['college_id']
    type_id = 2 #学院管理员权限等级是2

    teacher = Teacher.query.filter_by(number = request.json['number']).first()
    if teacher:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '改账号已存在'
        })
    if not college_id:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '请填写学院'
        })
    teacher = Teacher()
    teacher.number = number
    teacher.password = password
    teacher.type = type
    db.session.add(teacher)
    db.session.commit()

    teacherInfo = TeacherInfo()
    teacherInfo.number = number
    teacherInfo.college_id = college_id
    teacherInfo.type_id = type_id
    db.session.add(teacherInfo)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '添加成功'
    })

'''
    增加院级管理员 创建账号
'''
@sadmin.route('/secretary/reset_password', methods=['GET', 'POST'])
def resetPassword():
    number = request.json['number']
    teacher = Teacher.query.filter_by(number = number).first()
    if teacher:
        teacher.password = generate_password_hash( '123456' ) #初始化密码默认为 123456
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '重设密码成功'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '不存在此管理员账号'
        })
'''
    删除管理员账号
'''
@sadmin.route('/secretary/delete', methods=['GET', 'POST'])
def deleteSecretary():
    number = request.json['number']

    teacherInfo = TeacherInfo.query.filter_by(number=number).first()
    teacher = Teacher.query.filter_by(number=number).first()

    db.session.delete(teacherInfo)
    db.session.commit()

    db.session.delete(teacher)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '删除成功'
    })



'''
    【查询】学院管理员详细信息查询 by 院级管理员名字 或者 学院名称 模糊查询
'''
@sadmin.route('/secretary/search', methods=['GET', 'POST'])
def searchSecretary():
    search_type = request.json['search_type']
    search_value = request.json['search_value']
    if search_type == '' and search_value == '':
        secretary = db.session.query( TeacherInfo.number, College.name.label('college_name')  ) \
            .join(College, TeacherInfo.college_id == College.id) \
            .filter(TeacherInfo.type_id == 2).all()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(secretary)
        })
    elif search_type == 'number':
        secretary = db.session.query( TeacherInfo.number, College.name.label('college_name') ) \
            .join(College, TeacherInfo.college_id == College.id) \
            .filter(and_(TeacherInfo.type_id==2, TeacherInfo.number.like('%' + search_value + '%'))).all()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(secretary)
        })
    elif search_type == 'college_name':
        secretary = db.session.query( TeacherInfo.number, College.name.label('college_name') ) \
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




'''

    废弃


#【更改】撤销指定教师的教务秘书职位 by TeacherInfo.id  把教师是院级管理员的身份改为普通教师
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


#更改 院级管理员的 电话 mail信息 by TeacherInfo.number
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