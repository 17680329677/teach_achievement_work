from flask import jsonify, request
from app.api_1_0.normal import normal

from app import db
from app.models import TeacherInfo,College,TeachReformProject,TeacherProject,ProjectChildType,ProjectRank,ProjectChangeRecord
from JSONHelper import JSONHelper
import time

'''
    教改项目
'''

'''
    获得本学院 教改项目信息 by token 并且状态 status ！= 1
'''
@normal.route('/teach_reform/index', methods=['GET', 'POST'])
def getAllTeachReformInfo():
    teacherToken = request.json['token']  # token 是教师的工号

    teach_reform = db.session.query(TeachReformProject.id.label('id'), \
                                    TeachReformProject.project_name.label('project_name'), \
                                    TeachReformProject.project_number.label('project_number'), \
                                    TeacherInfo.name.label('teacher_name'), \
                                    ProjectRank.rank_name.label('rank_name'),\
                                    TeachReformProject.status.label('status'), \
                                    TeachReformProject.submit_time.label('submit_time'), \
                                    ) \
        .join(TeacherProject, TeachReformProject.id == TeacherProject.project_id)\
        .join(TeacherInfo,TeacherInfo.number == TeacherProject.teacher_number) \
        .join(ProjectRank, ProjectRank.id == TeachReformProject.rank_id) \
        .filter(TeacherProject.teacher_number == teacherToken)\
        .order_by(TeachReformProject.submit_time.desc()).all()
    if teach_reform:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(teach_reform)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '项目为空!'
        })

'''
    获得教改项目的详细信息 by .id
'''
@normal.route('/teach_reform/detail', methods=['GET', 'POST'])
def getTeachReformInfo():
    projectId = request.json['id']
    detail_info = db.session.query( TeachReformProject.id.label('id'),\

                                    TeacherInfo.number.label('teacher_name'),\
                                    TeacherProject.participate_type.label('participate_type'),\

                                    TeachReformProject.project_name.label('project_name'),\
                                    TeachReformProject.project_number.label('project_number'),\

                                    TeachReformProject.type_child_id.label('type_child_id'),\
                                    ProjectChildType.child_type_name.label('child_type_name'),\

                                    TeachReformProject.rank_id.label('rank_id'),\
                                    ProjectRank.rank_name.label('rank_name'),\

                                    TeachReformProject.college_id.label('college_id'),\
                                    TeachReformProject.begin_year_month.label('begin_year_month'),\
                                    TeachReformProject.mid_check_year_month.label('mid_check_year_month'),\
                                    TeachReformProject.end_year_month.label('end_year_month'),\
                                    TeachReformProject.mid_check_rank.label('mid_check_rank'),\
                                    TeachReformProject.end_check_rank.label('end_check_rank'),\
                                    TeachReformProject.subject.label('subject'),\
                                    TeachReformProject.status.label('status'),\
                                    TeachReformProject.host_student.label('host_student'),\
                                    TeachReformProject.participate_student.label('participate_student'),\
                                    TeachReformProject.remark.label('remark'),\
                                    TeachReformProject.grade.label('grade'),\
                                    TeachReformProject.funds.label('funds'),\
                                    TeachReformProject.submit_time.label('submit_time')   )\
        .join(ProjectChildType, ProjectChildType.id == TeachReformProject.type_child_id)\
        .join(ProjectRank, ProjectRank.id == TeachReformProject.rank_id)\
        .join(College, TeachReformProject.college_id == College.id)\
        .join(TeacherProject, TeacherProject.project_id == TeachReformProject.id) \
        .join(TeacherInfo, TeacherInfo.number == TeacherProject.teacher_number) \
        .filter(TeachReformProject.id == projectId).all()

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
            'reason': 'something was wrong!'
        })


'''
    添加教改项目信息
'''
@normal.route('/teach_reform/create', methods=['GET', 'POST'])
def teacherReformProjectCreate():
    teacherToken = request.json['token']  # token 是教师的工号
    cadminInfo = TeacherInfo.query.filter_by(number=teacherToken).first()
    collegeId = cadminInfo.college_id

    createError = 0
    errorMsg = ''

    if not collegeId:
        createError = 1
        errorMsg = '您的账号信息没有对应的学院'

    participateType = request.json['participate_type'] #不是空，参与类型（负责人、参与人）

    project_name = request.json['project_name'] #不是空
    project_number = request.json['project_number'] #不是空
    type_child_id = int( request.json['type_child_id'] ) #不是空，在project_type_child有对应
    rank_id = int( request.json['rank_id'] ) #不是空
    college_id = collegeId #不是空
    begin_year_month = request.json['begin_year_month']
    mid_check_year_month = request.json['mid_check_year_month']
    end_year_month = request.json['end_year_month']
    mid_check_rank = request.json['mid_check_rank']
    end_check_rank = request.json['end_check_rank']
    subject = request.json['subject']
    status = '1'
    host_student = request.json['host_student']
    participate_student = request.json['participate_student']
    remark = request.json['remark']
    grade = request.json['grade']
    submit_time = int(time.time())  #不是空

    if not project_name:
        createError = 1
        errorMsg = '教改项目名称不能为空'
    if not project_number:
        createError = 1
        errorMsg = '项目编号不能为空'

    projectChildType = ProjectChildType.query.filter_by(id = type_child_id).first()
    if not projectChildType:
        createError = 1
        errorMsg = '教改项目子类型id没有对应'
    if not type_child_id:
        createError = 1
        errorMsg = '项目子类型不能为空'

    rankId = ProjectRank.query.filter_by(id = rank_id).first()
    if not rankId:
        createError = 1
        errorMsg = '项目级别id没有对应'
    if not rank_id:
        createError = 1
        errorMsg = '项目级别不能为空'

    if not participateType:
        createError = 1
        errorMsg = '项目参与类型不能为空'

    if createError:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': errorMsg
        })

    #添加teacherpro
    teachReformProject = TeachReformProject()
    teachReformProject.project_name = project_name
    teachReformProject.project_number = project_number
    teachReformProject.type_child_id = type_child_id
    teachReformProject.rank_id = rank_id
    teachReformProject.college_id = college_id
    teachReformProject.begin_year_month = begin_year_month
    teachReformProject.mid_check_year_month = mid_check_year_month
    teachReformProject.end_year_month = end_year_month
    teachReformProject.mid_check_rank = mid_check_rank
    teachReformProject.end_check_rank = end_check_rank
    teachReformProject.subject = subject
    teachReformProject.status = status
    teachReformProject.host_student = host_student
    teachReformProject.participate_student = participate_student
    teachReformProject.remark = remark
    teachReformProject.grade = grade
    teachReformProject.submit_time = submit_time
    db.session.add(teachReformProject)
    db.session.commit()

    #添加teacher_project
    teacherProject = TeacherProject()
    teacherProject.teacher_number = teacherToken
    teacherProject.project_id = teachReformProject.id
    teacherProject.participate_type = participateType
    db.session.add(teacherProject)
    db.session.commit()
    
    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '添加成功'
    })

'''
    获取本项目变更记录 get project_change_record
'''
@normal.route('/teach_reform_project_change_record/get', methods=['GET', 'POST'])
def teacherReformProjectChangeRecordGet():
    project_id = request.json['project_id']
    projectChangeRecord = ProjectChangeRecord.query.filter_by(project_id = project_id).all()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': ProjectChangeRecord.to_json(projectChangeRecord )
    })


'''
    添加变更记录 project_change_record
'''
@normal.route('/teach_reform_project_change_record/create', methods=['GET', 'POST'])
def teacherReformProjectChangeRecordCreate():
    teacherToken = request.json['token']  # token 是教师的工号

    createError = 0
    errorMsg = ''

    project_id = request.json['project_id']
    reason = request.json['reason']
    change_time = request.json['change_time']
    describe = request.json['describe']

    if not describe:
        createError = 1
        errorMsg = '项目描述不能为空'
    if not change_time:
        createError = 1
        errorMsg = '变更时间不能为空'
    if not reason:
        createError = 1
        errorMsg = '变更原因不能为空'

    reformProject = TeachReformProject.query\
        .join(TeacherProject,TeacherProject.project_id == project_id)\
        .filter(TeachReformProject.id == project_id, TeacherProject.teacher_number == teacherToken).first()
    if not reformProject:
        createError = 1
        errorMsg = '此项目变更记录与您提交过的项目没有对应'
    else:
        if reformProject.status == '6':
            createError = 1
            errorMsg = reformProject.project_name + '此项目已存档，不能修改'
            #1本地编辑 2待审批 3立项 4中期检查通过 5结题 6存档

    if not project_id:
        createError = 1
        errorMsg = '项目不能为空'

    if createError:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': errorMsg
        })

    changeRecord = ProjectChangeRecord()
    changeRecord.project_id = project_id
    changeRecord.reason = reason
    changeRecord.change_time = change_time
    changeRecord.describe = describe
    db.session.add(changeRecord)
    db.session.commit()

    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '添加成功'
    })


'''
    修改教改项目信息
'''
@normal.route('/teach_reform/submitInfo/change', methods=['GET', 'POST'])
def changeSubmitReformInfo():
    teacherToken = request.json['token']  # token 是教师的工号
    cadminInfo = TeacherInfo.query.filter_by(number=teacherToken).first()
    collegeId = cadminInfo.college_id

    createError = 0
    errorMsg = ''

    if not collegeId:
        createError = 1
        errorMsg = '您的账号信息没有对应的学院'

    id = request.json['id']
    participate_type = request.json['participate_type']

    project_name = request.json['project_name']
    project_number = request.json['project_number']
    type_child_id = request.json['type_child_id']
    rank_id = request.json['rank_id']
    #college_id = request.json['college_id']
    begin_year_month = request.json['begin_year_month']
    mid_check_year_month = request.json['mid_check_year_month']
    end_year_month = request.json['end_year_month']
    mid_check_rank = request.json['mid_check_rank']
    end_check_rank = request.json['end_check_rank']
    subject = request.json['subject']
    #status = request.json['status']
    host_student = request.json['host_student']
    participate_student = request.json['participate_student']
    remark = request.json['remark']
    grade = request.json['grade']
    #funds = request.json['funds']
    #submit_time = request.json['submit_time']

    if not project_name:
        createError = 1
        errorMsg = '教改项目名称不能为空'
    if not project_number:
        createError = 1
        errorMsg = '项目编号不能为空'

    projectChildType = ProjectChildType.query.filter_by(id = type_child_id).first()
    if not projectChildType:
        createError = 1
        errorMsg = '教改项目子类型id没有对应'
    if not type_child_id:
        createError = 1
        errorMsg = '项目子类型不能为空'

    rankId = ProjectRank.query.filter_by(id = rank_id).first()
    if not rankId:
        createError = 1
        errorMsg = '项目级别id没有对应'
    if not rank_id:
        createError = 1
        errorMsg = '项目级别不能为空'

    if not participate_type:
        createError = 1
        errorMsg = '项目参与类型不能为空'

    teachReformProject = TeachReformProject.query.filter_by(id = id).first()

    if teachReformProject.status != '1':
        createError = 1
        errorMsg = '项目信息已提交或存档不能修改'

    if createError:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': errorMsg
        })

    teachReformProject.project_name = project_name
    teachReformProject.project_number = project_number
    teachReformProject.type_child_id = type_child_id
    teachReformProject.rank_id = rank_id
    #teachReformProject.college_id = college_id
    teachReformProject.begin_year_month = begin_year_month
    teachReformProject.mid_check_year_month = mid_check_year_month
    teachReformProject.end_year_month = end_year_month
    teachReformProject.mid_check_rank = mid_check_rank
    teachReformProject.end_check_rank = end_check_rank
    teachReformProject.subject = subject
    #teachReformProject.status = status
    teachReformProject.host_student = host_student
    teachReformProject.participate_student = participate_student
    teachReformProject.remark = remark
    teachReformProject.grade = grade
    #teachReformProject.funds = funds
    #teachReformProject.submit_time = submit_time

    teacherProject = TeacherProject.query.filter_by( project_id =  id ).first()
    teacherProject.participate_type = participate_type

    db.session.commit()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '修改成功'
    })

'''
    状态更变  
    status：状态：1未提交/本地编辑 2已提交/待审批 3立项 4中期检查通过 5结题 6存档
'''
@normal.route('/teach_reform/changestatus', methods=['GET', 'POST'])
def reformChangeStatus():
    id = request.json['id']
    status = request.json['status']
    teachReform = TeachReformProject.query.filter_by(id=id).first()
    if int(teachReform.status) > 2:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '已审批不可修改'
        })
    if teachReform:
        try:
            teachReform.status = status
            db.session.commit()
            return jsonify({
                'code': 20000,
                'status': 'success'
            })
        except:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '状态更变失败!'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '状态更变失败!'
        })


'''
    按状态搜索： 
    status：状态：1本地编辑 2待审批 3立项 4中期检查 5结题 6存档  ps：0全部搜索
'''
@normal.route('/teach_reform/status_search', methods=['GET', 'POST'])
def statusSearchTeachReform():
    teacherToken = request.json['token']  # token 是教师的工号

    status = request.json['status']

    teach_reforms = db.session.query(TeachReformProject.id.label('id'), \
                                    TeachReformProject.project_name.label('project_name'), \
                                     TeachReformProject.project_number.label('project_number'), \
                                     TeacherInfo.name.label('teacher_name'), \
                                    ProjectRank.rank_name.label('rank_name'),\
                                    TeachReformProject.status.label('status'), \
                                     TeachReformProject.submit_time.label('submit_time'), \
                                     ) \
        .join(TeacherProject, TeachReformProject.id == TeacherProject.project_id)\
        .join(TeacherInfo,TeacherInfo.number == TeacherProject.teacher_number) \
        .join(ProjectRank, ProjectRank.id == TeachReformProject.rank_id)
    if status != '0':
        teach_reforms = teach_reforms.filter(TeacherProject.teacher_number == teacherToken,  TeachReformProject.status == status )
    else:
        teach_reforms = teach_reforms.filter(TeacherProject.teacher_number == teacherToken)

    teach_reform = teach_reforms.order_by(TeachReformProject.submit_time.desc()).all()
    if teach_reform:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(teach_reform)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有匹配项目!'
        })

'''
    搜索
    根据 查询项目信息 by number  并且状态不为待提交
'''
@normal.route('/teach_reform/search', methods=['GET', 'POST'])
def searchTeachReformInfo():
    teacherToken = request.json['token']  # token 是教师的工号
    cadminInfo = TeacherInfo.query.filter_by(number=teacherToken).first()
    collegeId = cadminInfo.college_id

    search_type = request.json['search_type']
    search_value = request.json['search_value']
    teachReforms = db.session.query( TeachReformProject.id.label('id'), \
                                    TeachReformProject.project_name.label('project_name'), \
                                    TeachReformProject.project_number.label('project_number'), \
                                    TeacherInfo.name.label('teacher_name'), \
                                    ProjectRank.rank_name.label('rank_name'),\
                                    TeachReformProject.status.label('status') , \
                                     TeachReformProject.submit_time.label('submit_time'), \
                                     ) \
        .join(TeacherProject, TeachReformProject.id == TeacherProject.project_id)\
        .join(TeacherInfo,TeacherInfo.number == TeacherProject.teacher_number) \
        .join(ProjectRank, ProjectRank.id == TeachReformProject.rank_id)

    if search_type == '' and search_value == '':
        teachReform = teachReforms.filter(TeacherProject.teacher_number == teacherToken  ) \
            .order_by(TeachReformProject.submit_time.desc()).all()

    elif search_type == 'reform_name':
        teachReform = teachReforms\
            .filter(TeacherProject.teacher_number == teacherToken,  TeachReformProject.project_name.like('%' + search_value + '%') ) \
            .order_by(TeachReformProject.submit_time.desc()).all()

    elif search_type == 'teacher_name':
        teachReform = teachReforms\
            .filter(TeacherProject.teacher_number == teacherToken,  TeacherInfo.name.like('%' + search_value + '%') ) \
            .order_by(TeachReformProject.submit_time.desc()).all()

    elif search_type == '' and search_value != '':
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'please selected search type!'
        })


    if teachReform:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(teachReform)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'Found nothing!'
        })