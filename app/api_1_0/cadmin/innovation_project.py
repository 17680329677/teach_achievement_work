from flask import jsonify, request
from app.api_1_0.cadmin import cadmin

from app import db
from app.models import TeacherInfo,College,InnovationProject,InnovationTeacher,InnovationRank
from JSONHelper import JSONHelper

'''
    大创项目管理   (1未提交；2已提交；3已存档 ；) 
'''

'''
    获得本学院 大创项目总体信息 by token 并且状态 status ！= 1
'''
@cadmin.route('/innovation/index', methods=['GET', 'POST'])
def getAllInnovationInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id


    innovation = db.session.query(  InnovationProject.id.label('id'),\
                                    InnovationProject.project_name.label('project_name'),\
                                    InnovationProject.project_number.label('project_number'), \
                                    InnovationProject.status.label('status'),\
                                    InnovationRank.rank_name.label('rank_name'),\
                                    TeacherInfo.name.label('teacher_name'),\
                                    InnovationProject.end_check_rank.label('end_check_rank'),\
                                    InnovationProject.submit_time.label('submit_time'),\
                                 )\
        .join(InnovationRank, InnovationRank.id == InnovationProject.rank_id) \
        .join(InnovationTeacher, InnovationTeacher.project_id == InnovationProject.id) \
        .join(TeacherInfo, InnovationTeacher.teacher_number == TeacherInfo.number) \
        .filter(InnovationProject.college_id == collegeId,  InnovationProject.status != '1'  ).all()
    if innovation:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(innovation)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有大创项目!'
        })

'''
    获得某个大创项目的详细信息 by innovation.id
'''
@cadmin.route('/innovation/detail', methods=['GET', 'POST'])
def getDetailInnovationInfo():
    innovationId = request.json['id']


    detail_info = db.session.query(
                                    InnovationProject.id.label('id'), \

                                    TeacherInfo.name.label('teacher_name'),\
                                    TeacherInfo.number.label('teacher_number'),\

                                    InnovationProject.project_name.label('project_name'), \
                                    InnovationProject.project_number.label('project_number'), \
                                    InnovationProject.rank_id.label('rank_id'), \

                                    College.name.label('college_name'), \

                                    InnovationProject.begin_year_month.label('begin_year_month'), \
                                    InnovationProject.mid_check_year_month.label('mid_check_year_month'), \
                                    InnovationProject.end_year_month.label('end_year_month'), \
                                    InnovationProject.mid_check_rank.label('mid_check_rank'), \
                                    InnovationProject.end_check_rank.label('end_check_rank'), \
                                    InnovationProject.subject.label('subject'), \
                                    InnovationProject.status.label('status'), \
                                    InnovationProject.host_student.label('host_student'), \
                                    InnovationProject.participant_student.label('participant_student'), \
                                    InnovationProject.remark.label('remark'), \
                                    InnovationProject.submit_time.label('submit_time') \
                                ) \
        .join(College, InnovationProject.college_id == College.id) \
        .join(InnovationTeacher, InnovationTeacher.project_id == InnovationProject.id)\
        .join(TeacherInfo, InnovationTeacher.teacher_number == TeacherInfo.number)\
        .filter(InnovationProject.id == innovationId).all()

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
    修改大创项目信息
'''

@cadmin.route('/innovation/submitInfo/change', methods=['GET', 'POST'])
def changeInnovationSubmitInfo():
    id = request.json['id']
    project_name = request.json['project_name']
    project_number = request.json['project_number']
    rank_id = request.json['rank_id']
    begin_year_month = request.json['begin_year_month']
    mid_check_year_month = request.json['mid_check_year_month']
    end_year_month = request.json['end_year_month']
    mid_check_rank = request.json['mid_check_rank']
    end_check_rank = request.json['end_check_rank']
    subject = request.json['subject']
    status = request.json['status']
    host_student = request.json['host_student']
    participant_student = request.json['participant_student']
    remark = request.json['remark']

    innovationProject = InnovationProject.query.filter_by(id = id).first()

    innovationProject.id = id
    innovationProject.project_name = project_name
    innovationProject.project_number = project_number
    innovationProject.rank_id = rank_id
    innovationProject.begin_year_month = begin_year_month
    innovationProject.mid_check_year_month = mid_check_year_month
    innovationProject.end_year_month = end_year_month
    innovationProject.mid_check_rank = mid_check_rank
    innovationProject.end_check_rank = end_check_rank
    innovationProject.subject = subject
    innovationProject.status = status
    innovationProject.host_student = host_student
    innovationProject.participant_student = participant_student
    innovationProject.remark = remark

    db.session.commit()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': ''
    })

'''
    状态更变  [  状态（展示）普通用户角色显示：(1未提交；2已提交；3已存档 ；)    管理员角色显示：(2待审批；3已存档；)   ]
'''

@cadmin.route('/innovation/changestatus', methods=['GET', 'POST'])
def changeInnovationStatus():
    id = request.json['id']
    status = request.json['status']
    innovation = InnovationProject.query.filter_by(id = id).first()
    if innovation:
        try:
            innovation.status = status
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
@cadmin.route('/innovation/status_search', methods=['GET', 'POST'])
def statusSearchInnovation():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    status = request.json['status']

    innovations = db.session.query(     InnovationProject.id.label('id'),\
                                        InnovationProject.project_name.label('project_name'),\
                                        InnovationProject.project_number.label('project_number'), \
                                        InnovationProject.status.label('status'), \

                                        InnovationRank.rank_name.label('rank_name'),\
                                        TeacherInfo.name.label('teacher_name'),\

                                        InnovationProject.end_check_rank.label('end_check_rank'),\
                                        InnovationProject.submit_time.label('submit_time'),\
                                 )\
        .join(InnovationRank, InnovationRank.id == InnovationProject.rank_id) \
        .join(InnovationTeacher, InnovationTeacher.project_id == InnovationProject.id) \
        .join(TeacherInfo, InnovationTeacher.teacher_number == TeacherInfo.number)
    if status != '0':
        innovations = innovations.filter(InnovationProject.college_id == collegeId,  InnovationProject.status == status )
    else:
        innovations = innovations.filter(InnovationProject.college_id == collegeId)

    innovation = innovations.order_by(InnovationProject.submit_time.desc()).all()
    if innovation:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(innovation)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有匹配项目!'
        })

'''
    按大创项目名词和教师姓名搜索
    根据 查询项目信息 by number   并且状态不为待提交
'''

@cadmin.route('/innovation/search', methods=['GET', 'POST'])
def searchInovationInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    search_type = request.json['search_type']
    search_value = request.json['search_value']
    innovations = db.session.query(    InnovationProject.id.label('id'),\
                                        InnovationProject.project_name.label('project_name'),\
                                        InnovationProject.project_number.label('project_number'),\


                                        InnovationRank.rank_name.label('rank_name'),\
                                        TeacherInfo.name.label('teacher_name'),\

                                        InnovationProject.end_check_rank.label('end_check_rank'),\
                                        InnovationProject.submit_time.label('submit_time'),\
                                 )\
        .join(InnovationRank, InnovationRank.id == InnovationProject.rank_id) \
        .join(InnovationTeacher, InnovationTeacher.project_id == InnovationProject.id) \
        .join(TeacherInfo, InnovationTeacher.teacher_number == TeacherInfo.number)

    if search_type == '' and search_value == '':
        innovations = innovations.filter(InnovationProject.college_id == collegeId,InnovationProject.status != '1')

    elif search_type == 'project_name':
        innovations = innovations \
            .filter(InnovationProject.college_id == collegeId,
                    InnovationProject.project_name.like('%' + search_value + '%'), InnovationProject.status != '1')

    elif search_type == 'teacher_name':
        innovations = innovations \
            .filter(InnovationProject.college_id == collegeId, TeacherInfo.name.like('%' + search_value + '%'),
                    InnovationProject.status != '1')

    elif search_type == '' and search_value != '':
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'please selected search type!'
        })

    innovation = innovations.order_by(InnovationProject.submit_time.desc()).all()
    if innovation:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(innovation)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有匹配到该项目!'
        })