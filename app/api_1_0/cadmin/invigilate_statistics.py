from flask import jsonify, request
from app.api_1_0.cadmin import cadmin

from collections import Counter
from app import db
from app.models import TeacherInfo,College,InvigilateInfo,SemesterInfo
from JSONHelper import JSONHelper

'''
    监考信息统计   (1未提交；2已提交；3已存档 ；) 
'''

'''
    获得本学院 统计监考信息 by token && 状态 status == 3
'''
@cadmin.route('/invigilate_statistics/index', methods=['GET', 'POST'])
def getInvigilateStatisticsInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    #只从已存档的信息中统计
    invigilates = InvigilateInfo.query.filter(InvigilateInfo.college_id == collegeId, InvigilateInfo.status == '3').all()

    participaters = []

    if invigilates:
        for invigilate in invigilates:
            participater = invigilate.participate_teacher.split(",")
            if participater:
                for part in participater:
                    participaters.append(part)
            #participaters.append(invigilate.apply_teacher) # 这里不追加申请人了。如果申请人参与了监考，那就在participate_teacher中包含申请人。统计监考次数的时候只统计participate_teacher中的工号。因为申请人有可能没参加监考。）

        #统计每个教师出现的次数 apply_teacher + participate_teacher
        countResult = Counter(participaters)
        #print(countResult)  #Counter({'5000010': 3, '7180266': 2, '5003': 1, '7180278': 1, '7180288': 1})

        data = []
        for key in countResult.keys():
            #print(key, '+', countResult[key])
            teacher_number = key
            invigilate_times = countResult[key]
            teacherInfo = db.session.query(TeacherInfo.number, TeacherInfo.name, TeacherInfo.status,).filter(TeacherInfo.number == teacher_number).first()
            teacherInfo = JSONHelper.jsonBQfirst(teacherInfo)
            teacherInfo['invigilate_times'] = invigilate_times
            #print(teacherInfo)  #追加invigilate_times后 {'number': '7180266', 'name': '普通66', 'status': None, 'invigilate_times': 2}
            data.append(teacherInfo)

        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': data
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有监考信息!'
        })



'''
    按照时间段 统计监考信息
'''
@cadmin.route('/invigilate_statistics/time_section', methods=['GET', 'POST'])
def getInvigilateStatisticsTimeSectionInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    #时间段
    fromTime = request.json['from_time']
    toTime = request.json['to_time']
    if fromTime > toTime:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '时间顺序错误'
        })

    if not fromTime:
        fromTime = 0

    # 只从已存档的且在时间范围内的 信息中统计
    if not toTime:
        invigilates = InvigilateInfo.query.filter(  InvigilateInfo.college_id == collegeId, \
                                                InvigilateInfo.submit_time >= fromTime,\
                                                InvigilateInfo.status == '3').all()
    else:
        invigilates = InvigilateInfo.query.filter(InvigilateInfo.college_id == collegeId, \
                                                  InvigilateInfo.submit_time >= fromTime, \
                                                  InvigilateInfo.submit_time <= toTime, \
                                                  InvigilateInfo.status == '3').all()

    participaters = []

    if invigilates:
        for invigilate in invigilates:
            participater = invigilate.participate_teacher.split(",")
            if participater:
                for part in participater:
                    participaters.append(part)
            # participaters.append(invigilate.apply_teacher) # 这里不追加申请人了。如果申请人参与了监考，那就在participate_teacher中包含申请人。统计监考次数的时候只统计participate_teacher中的工号。因为申请人有可能没参加监考。）

        # 统计每个教师出现的次数 apply_teacher + participate_teacher
        countResult = Counter(participaters)
        # print(countResult)  #Counter({'5000010': 3, '7180266': 2, '5003': 1, '7180278': 1, '7180288': 1})

        data = []
        for key in countResult.keys():
            # print(key, '+', countResult[key])
            teacher_number = key
            invigilate_times = countResult[key]
            teacherInfo = db.session.query(TeacherInfo.number, TeacherInfo.name, TeacherInfo.status, ).filter(
                TeacherInfo.number == teacher_number).first()
            teacherInfo = JSONHelper.jsonBQfirst(teacherInfo)
            teacherInfo['invigilate_times'] = invigilate_times
            # print(teacherInfo)  #追加invigilate_times后 {'number': '7180266', 'name': '普通66', 'status': None, 'invigilate_times': 2}
            data.append(teacherInfo)

        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': data
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有监考信息!'
        })


'''
    获得本教师详细监考历史（统计教师再apply_teacher or participate_teacher 出现过 就可以显示） 并且是已经审核通过的
'''
@cadmin.route('/invigilate_statistics/detail', methods=['GET', 'POST'])
def getInvigilateStatisticsDetailInfo():
    teacher_number = request.json['teacher_number']

    detail_info = db.session.query(
                    InvigilateInfo.id.label('id'), \
                    InvigilateInfo.apply_teacher.label('apply_teacher_number'), \
                    TeacherInfo.name.label('apply_teacher_name'), \
                    InvigilateInfo.subject.label('subject'), \
                    InvigilateInfo.semester_id.label('semester_id'), \
                    InvigilateInfo._class.label('_class'), \
                    InvigilateInfo.college_id.label('college_id'), \
                    InvigilateInfo.exam_time.label('exam_time'), \
                    InvigilateInfo.location.label('location'), \
                    InvigilateInfo.participate_teacher.label('participate_teacher'), \
                    InvigilateInfo.submit_time.label('submit_time'), \
                    InvigilateInfo.status.label('status'), \
                    ) \
        .join(College, InvigilateInfo.college_id == College.id) \
        .join(TeacherInfo, InvigilateInfo.apply_teacher == TeacherInfo.number) \
        .filter( InvigilateInfo.participate_teacher.like('%' + teacher_number + '%'), InvigilateInfo.status == '3' ).all()

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