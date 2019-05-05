from flask import jsonify, request
from app.api_1_0.cadmin import cadmin

from app import db
from app.models import TeacherInfo,College,TeachReformProject,TeacherProject,ProjectChildType,ProjectRank
from JSONHelper import JSONHelper

'''
    教改项目
'''

'''
    获得本学院 教改项目信息 by token 并且状态 status ！= 1
'''
@cadmin.route('/teach_reform/index', methods=['GET', 'POST'])
def getAllTeachReformInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

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
        .filter(TeachReformProject.college_id == collegeId,  TeachReformProject.status != '1' )\
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
@cadmin.route('/teach_reform/detail', methods=['GET', 'POST'])
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
    修改教改项目信息
'''
@cadmin.route('/teach_reform/submitInfo/change', methods=['GET', 'POST'])
def changeSubmitReformInfo():
    id = request.json['id']
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

    teachReformProject = TeachReformProject.query.filter_by(id = id).first()
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

    db.session.commit()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': ''
    })

'''
    状态更变  
    status：状态：1未提交/本地编辑 2已提交/待审批 3立项 4中期检查通过 5结题 6存档
'''
@cadmin.route('/teach_reform/changestatus', methods=['GET', 'POST'])
def reformChangeStatus():
    id = request.json['id']
    status = request.json['status']
    teachReform = TeachReformProject.query.filter_by(id=id).first()
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
                'reason': '撤销提交失败!'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '撤销提交失败!'
        })


'''
    按状态搜索： 
    status：状态：1本地编辑 2待审批 3立项 4中期检查 5结题 6存档  ps：0全部搜索
'''
@cadmin.route('/teach_reform/status_search', methods=['GET', 'POST'])
def statusSearchTeachReform():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

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
        teach_reforms = teach_reforms.filter(TeachReformProject.college_id == collegeId,  TeachReformProject.status == status )
    else:
        teach_reforms = teach_reforms.filter(TeachReformProject.college_id == collegeId)

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
    根据 查询项目信息 by number   并且状态不为待提交
'''
@cadmin.route('/teach_reform/search', methods=['GET', 'POST'])
def searchTeachReformInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
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
        teachReform = teachReforms.filter(TeachReformProject.college_id == collegeId, TeachReformProject.status != '1') \
            .order_by(TeachReformProject.submit_time.desc()).all()

    elif search_type == 'reform_name':
        teachReform = teachReforms\
            .filter(TeachReformProject.college_id == collegeId, TeachReformProject.project_name.like('%' + search_value + '%'), TeachReformProject.status != '1') \
            .order_by(TeachReformProject.submit_time.desc()).all()

    elif search_type == 'teacher_name':
        teachReform = teachReforms\
            .filter(TeachReformProject.college_id == collegeId, TeacherInfo.name.like('%' + search_value + '%'), TeachReformProject.status != '1') \
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