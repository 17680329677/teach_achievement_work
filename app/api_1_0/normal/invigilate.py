from flask import jsonify, request
from app.api_1_0.normal import normal

from app import db
from app.models import TeacherInfo,College,InvigilateInfo,SemesterInfo
from JSONHelper import JSONHelper
import time

'''
    监考信息管理   (1未提交；2已提交；3已存档 ；) 
'''

'''
    获得本学院 监考信息总体信息 by token 并且状态 status ！= 1
'''
@normal.route('/invigilate/index', methods=['GET', 'POST'])
def getAllInvigilateInfo():
    teacherToken = request.json['token']  # token 是教师的工号


    invigilate = db.session.query(  InvigilateInfo.id.label('id'),\
                                    InvigilateInfo.apply_teacher.label('apply_teacher_number'), \
                                    TeacherInfo.name.label('apply_teacher_name'),\
                                    InvigilateInfo.subject.label('subject'), \
                                    SemesterInfo.semester_name.label('semester_name'),\
                                    InvigilateInfo.participate_teacher.label('participate_teacher'),\
                                    InvigilateInfo.submit_time.label('submit_time'),\
                                    InvigilateInfo.status.label('status'),\
                                 )\
        .join(TeacherInfo, InvigilateInfo.apply_teacher == TeacherInfo.number) \
        .join(SemesterInfo, SemesterInfo.id == InvigilateInfo.semester_id) \
        .filter(InvigilateInfo.apply_teacher == teacherToken ).all()
    if invigilate:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(invigilate)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有监考信息!'
        })

'''
    获得某个监考信息的详细信息 by .id
'''
@normal.route('/invigilate/detail', methods=['GET', 'POST'])
def getDetailInvigilateInfo():
    invigilateId = request.json['id']


    detail_info = db.session.query(
                                    InvigilateInfo.id.label('id'), \
                                    InvigilateInfo.apply_teacher.label('apply_teacher_number'), \
                                    TeacherInfo.name.label('apply_teacher_name'), \
                                    InvigilateInfo.subject.label('subject'), \
                                    InvigilateInfo.semester_id.label('semester_id'), \
                                    SemesterInfo.semester_name.label('semester_name'),\
                                    InvigilateInfo._class.label('_class'), \
                                    InvigilateInfo.college_id.label('college_id'), \
                                    InvigilateInfo.exam_time.label('exam_time'), \
                                    InvigilateInfo.location.label('location'), \
                                    InvigilateInfo.participate_teacher.label('participate_teacher'), \
                                    InvigilateInfo.submit_time.label('submit_time'), \
                                    InvigilateInfo.status.label('status'), \
                                    ) \
        .join(SemesterInfo, SemesterInfo.id == InvigilateInfo.semester_id) \
        .join(TeacherInfo, InvigilateInfo.apply_teacher == TeacherInfo.number) \
        .filter(InvigilateInfo.id == invigilateId).all()

    if detail_info:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(detail_info)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '获取详细信息失败!'
        })


'''
    添加监考信息信息
'''
@normal.route('/invigilate/create', methods=['GET', 'POST'])
def invigilateCreate():
    teacherToken = request.json['token']  # token 是教师的工号
    cadminInfo = TeacherInfo.query.filter_by(number=teacherToken).first()
    collegeId = cadminInfo.college_id

    createError = 0
    errorMsg = ''

    if not collegeId:
        createError = 1
        errorMsg = '您的账号信息没有对应的学院'

    apply_teacher = teacherToken #不为空
    subject = request.json['subject'] #不为空
    semester_id = request.json['semester_id'] #如果有必须有匹配
    _class = request.json['_class'] #不为空
    college_id = collegeId #不为空
    exam_time = request.json['exam_time']
    location = request.json['location'] #不为空
    participate_teacher = request.json['participate_teacher'] #不为空，至少有一个教师工号，不一定是自己
    submit_time = int(time.time())  #不是空
    status = '1'

    if semester_id:
        semester = SemesterInfo.query.filter_by(id = semester_id).first()
        if not semester:
            createError = 1
            errorMsg = '所属学期id没有对应'
    if not subject:
        createError = 1
        errorMsg = '考试科目不能为空'
    if not _class:
        createError = 1
        errorMsg = '参加考试的班级不能为空'
    if not location:
        createError = 1
        errorMsg = '考试地点不能为空'
    if not participate_teacher:
        createError = 1
        errorMsg = '参与监考教师不能为空'

    if createError:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': errorMsg
        })

    invigilate = InvigilateInfo()
    invigilate.apply_teacher = apply_teacher
    invigilate.subject = subject
    invigilate.semester_id = semester_id
    invigilate._class = _class
    invigilate.college_id = college_id
    invigilate.exam_time = exam_time
    invigilate.location = location
    invigilate.participate_teacher = participate_teacher
    invigilate.submit_time = submit_time
    invigilate.status = status
    db.session.add(invigilate)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '添加成功'
    })


'''
    修改监考信息信息
'''
@normal.route('/invigilate/submitInfo/change', methods=['GET', 'POST'])
def changeInvigilateSubmitInfo():
    teacherToken = request.json['token']  # token 是教师的工号
    cadminInfo = TeacherInfo.query.filter_by(number=teacherToken).first()
    collegeId = cadminInfo.college_id

    createError = 0
    errorMsg = ''

    if not collegeId:
        createError = 1
        errorMsg = '您的账号信息没有对应的学院'

    id = request.json['id']
    subject = request.json['subject']
    semester_id = request.json['semester_id']
    _class = request.json['_class']
    exam_time = request.json['exam_time']
    location = request.json['location']
    participate_teacher = request.json['participate_teacher']

    if semester_id:
        semester = SemesterInfo.query.filter_by(id = semester_id).first()
        if not semester:
            createError = 1
            errorMsg = '所属学期id没有对应'
    if not subject:
        createError = 1
        errorMsg = '考试科目不能为空'
    if not _class:
        createError = 1
        errorMsg = '参加考试的班级不能为空'
    if not location:
        createError = 1
        errorMsg = '考试地点不能为空'
    if not participate_teacher:
        createError = 1
        errorMsg = '参与监考教师不能为空'

    if createError:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': errorMsg
        })

    invigilate = InvigilateInfo.query.filter_by(id = id).first()

    invigilate.subject = subject
    invigilate.semester_id = semester_id
    invigilate._class = _class
    invigilate.exam_time = exam_time
    invigilate.location = location
    invigilate.participate_teacher = participate_teacher

    db.session.commit()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': ''
    })

'''
    状态更变  [  状态（展示）普通用户角色显示：(1未提交；2已提交；3已存档；)    教师角色显示：(2待审批；3已存档；)   ]
'''
@normal.route('/invigilate/changestatus', methods=['GET', 'POST'])
def changeInvigilateStatus():
    id = request.json['id']
    status = request.json['status']
    invigilate = InvigilateInfo.query.filter_by(id = id).first()
    if invigilate:
        try:
            invigilate.status = status
            db.session.commit()
            return jsonify({
                'code': 20000,
                'status': 'success'
            })
        except:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '状态更新成功!'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '状态更新失败!'
        })


'''
    按状态搜索： 
    status：状态：1未提交、2提交/待审核、3存档/已审核   ps：0全部搜索
'''
@normal.route('/invigilate/status_search', methods=['GET', 'POST'])
def statusSearchInvigilate():
    teacherToken = request.json['token']  # token 是教师的工号

    status = request.json['status']

    invigilates = db.session.query( InvigilateInfo.id.label('id'),\
                                    InvigilateInfo.apply_teacher.label('apply_teacher_number'), \
                                    TeacherInfo.name.label('apply_teacher_name'),\
                                    InvigilateInfo.subject.label('subject'), \
                                    SemesterInfo.semester_name.label('semester_name'),\
                                    InvigilateInfo.participate_teacher.label('participate_teacher'),\
                                    InvigilateInfo.submit_time.label('submit_time'),\
                                    InvigilateInfo.status.label('status'),\
                                 )\
        .join(TeacherInfo, InvigilateInfo.apply_teacher == TeacherInfo.number)\
        .join(SemesterInfo, SemesterInfo.id == InvigilateInfo.semester_id) \

    if status != '0':
        invigilates = invigilates.filter(InvigilateInfo.apply_teacher == teacherToken,  InvigilateInfo.status == status )
    else:
        invigilates = invigilates.filter(InvigilateInfo.apply_teacher == teacherToken)

    invigilate = invigilates.order_by(InvigilateInfo.submit_time.desc()).all()
    if invigilate:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(invigilate)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有匹配项目!'
        })

'''
    按监考信息考试课程和教师姓名搜索
    根据 查询项目信息 by number   并且状态不为待提交
'''

@normal.route('/invigilate/search', methods=['GET', 'POST'])
def searchInvigilateInfo():
    teacherToken = request.json['token']  # token 是教师的工号

    search_type = request.json['search_type']
    search_value = request.json['search_value']
    invigilates = db.session.query(  InvigilateInfo.id.label('id'),\
                                    InvigilateInfo.apply_teacher.label('apply_teacher_number'), \
                                    TeacherInfo.name.label('apply_teacher_name'),\
                                    InvigilateInfo.subject.label('subject'), \
                                    SemesterInfo.semester_name.label('semester_name'),\
                                    InvigilateInfo.participate_teacher.label('participate_teacher'),\
                                    InvigilateInfo.submit_time.label('submit_time'),\
                                    InvigilateInfo.status.label('status'),\
                                 )\
        .join(TeacherInfo, InvigilateInfo.apply_teacher == TeacherInfo.number)\
        .join(SemesterInfo, SemesterInfo.id == InvigilateInfo.semester_id) \

    if search_type == '' and search_value == '':
        invigilates = invigilates.filter(InvigilateInfo.apply_teacher == teacherToken)

    elif search_type == 'invigilate_name':
        invigilates = invigilates \
            .filter(InvigilateInfo.apply_teacher == teacherToken,InvigilateInfo.subject.like('%' + search_value + '%')  )

    elif search_type == 'teacher_name':
        invigilates = invigilates \
            .filter(InvigilateInfo.apply_teacher == teacherToken, TeacherInfo.name.like('%' + search_value + '%')  )

    elif search_type == '' and search_value != '':
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'please selected search type!'
        })

    invigilate = invigilates.order_by(InvigilateInfo.submit_time.desc()).all()
    if invigilate:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(invigilate)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有匹配到该监考信息!'
        })