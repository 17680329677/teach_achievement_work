from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json

from JSONHelper import JSONHelper
from app import db
from app.models import Student,DistributionDesire,TeacherInfo,DistributionInfo,DistributionResult

import time

'''
    ----------------------------分流志愿填报情况-------------------------
'''

'''
    显示所有分流志愿
'''
@cadmin.route('/distribution_desire/get',methods=['GET','POST'])
def getDistributionDesire():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    students = Student.query.filter_by(college_id = collegeId).all() # model对象的list
    students = Student.to_json(students)  # json 数组
    #print(students)
    for student in students:
        del student['password'] #不现实密码
        distributionDesire = DistributionDesire.query.filter_by(student_id = student["id"]).all()
        student['desire'] = DistributionDesire.to_json(distributionDesire)
    #print(students)

    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': students
    })

'''
    按是否填报搜索： 
    if_choose : "已填报" / "未填报"
'''
@cadmin.route('/distribution_desire/status_search', methods=['GET', 'POST'])
def statusSearchDistributionDesire():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    if_choose = request.json['if_choose']

    tempList = []

    students = Student.query.filter_by(college_id = collegeId).all()  # model对象的list
    students = Student.to_json(students)  # json 数组
    for student in students:
        del student['password']  #不现实密码
        distributionDesire = DistributionDesire.query.filter_by(student_id=student["id"]).all()
        if if_choose == '已填报':
            if distributionDesire:
                student['desire'] = DistributionDesire.to_json(distributionDesire)
                tempList.append(student) #将填报了志愿的学生加入到新list中
        elif if_choose == '未填报':
            if not distributionDesire:
                student['desire'] = DistributionDesire.to_json(distributionDesire)
                tempList.append(student) #将 没有 填写志愿的学生加入到新list中
        else: # '全部'
            student['desire'] = DistributionDesire.to_json(distributionDesire)
            tempList.append(student)  # 将 没有 填写志愿的学生加入到新list中

    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': tempList
    })


'''
    按照条件 查找分流志愿信息
'''
'''
    ************** 一键分流  ******************
    vue请求超时时间：5秒
    需要测试时间 
'''
@cadmin.route('/distribution_desire/distribute', methods=['GET', 'POST'])
def distributionDesireDistribute():
    '''
    专业分流规定：
    1.每个学生选满全部志愿。就是给今年的志愿排个序（除了优秀专业，都必须排）。
    2.如果想选优秀班的首先处理。专业班也算普通志愿配置，只不过专业名称应配置为“优秀班”，且一个学院只能有一个“优秀班”专业。 ps：信息学院全称应该是“计算机创新实验班”。
    3.优秀班的志愿排名是0，其他从1开始
    4.下一轮处理时，筛选出未分配的学生做gpa排名。
    '''
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    # 1.对“优秀班的专业”做处理-------------------------------------------------------
    outStandingName = "优秀" #优秀班查找的关键字
    outStandingDistribution = DistributionInfo.query\
        .filter(DistributionInfo.college_id == collegeId ,DistributionInfo.orientation_name.like('%' + outStandingName + '%') ).first()
    if outStandingDistribution:
        outStandingId = outStandingDistribution.id #优秀专业的id
        #填报了优秀专业的同学，并且按照GPA从高到低依次排名。
        wantOutStandStudents = DistributionDesire.query.filter(DistributionDesire.college_id == collegeId, \
                                                               DistributionDesire.desire_rank == 0,\
                                                               DistributionDesire.distribution_id == outStandingId)\
            .join(Student, Student.id == DistributionDesire.student_id)\
            .order_by(Student.gpa.desc())\
            .all()
        distributeLimit = outStandingDistribution.num_limit #专业人数限制
        distributeTimes = 0 #当前分配的次数
        for wantStudent in wantOutStandStudents:
            haveStudent = DistributionResult.query.filter_by(student_id = wantStudent.student_id).first()
            if haveStudent:
                studentId = str(haveStudent.student_id)
                print('err student : ' + studentId)
                return jsonify({
                    'code': 20001,
                    'status': 'failed',
                    'reason': '学生学号：' + studentId + ' 已分配过专业（outStand ERROR），或已做过分流工作'
                })

            else:
                distributeTimes = distributeTimes + 1
                if distributeTimes <= distributeLimit:
                    distributionResult = DistributionResult()
                    distributionResult.college_id = collegeId
                    distributionResult.student_id = wantStudent.student_id
                    distributionResult.distribution_id = outStandingId
                    distributionResult.status = '0'
                    db.session.add(distributionResult)
                    db.session.commit()
                    print('outStand: ' + str(wantStudent.student_id) + ' commit ok')
                else:
                    break

    # 2.对普通班专业的学生做处理-------------------------------------------------------
    #有多少个专业就有多少个志愿，普通志愿 = 总志愿数 - 1
    #1.对优秀专业的查找做屏蔽
    if not outStandingDistribution:
        distributionObjs = DistributionInfo.query.filter(DistributionInfo.college_id == collegeId)
        print('this colloge (' + str(collegeId) + ') don\'t have brilliant distribution ')
    else:
        distributionObjs = DistributionInfo.query.filter(DistributionInfo.college_id == collegeId, \
                                                         DistributionInfo.id != outStandingDistribution.id)

    distributionNumber = distributionObjs.count()  # 有多少个专业 就有多少个志愿可选。
    distributionInfo = distributionObjs.all()
    #print(distributionInfo)

    if not distributionObjs:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '该学院还没有配置专业方向'
        })
    else:
        #因为循环从 1 ~ (distributionNumber - 1)，已屏蔽优秀专业所以+1
        for desireRank in range(1,distributionNumber+1):
            #print('第 ' + str(desireRank) +' 轮志愿录取工作：')

            #在每一轮志愿录取中，各个(专业/方向)录取学生
            for distribution in distributionInfo:
                #print(distribution.orientation_name)
                distributionId = distribution.id #此专业id

                #此专业在此轮志愿中有那些学生报名了，并按照GPA降序
                desireStudents = DistributionDesire.query\
                    .join(Student, Student.id == DistributionDesire.student_id)\
                    .filter(DistributionDesire.college_id == collegeId, \
                            DistributionDesire.desire_rank == desireRank, \
                            DistributionDesire.distribution_id == distributionId,)\
                    .order_by(Student.gpa.desc())\
                    .all()

                distributeLimit = distribution.num_limit  # 专业人数限制
                distributeTimes = 0  # 当前分配的次数
                #开始对此专业分配学生：
                for wantStudent in desireStudents:
                    haveDistributeStudent = DistributionResult.query.filter_by(student_id=wantStudent.student_id).first()
                    if haveDistributeStudent:
                        studentId = str(haveDistributeStudent.student_id)
                        print('jump distributed student : ' + studentId)
                    else:
                        distributeTimes = distributeTimes + 1
                        if distributeTimes <= distributeLimit:
                            distributionResult = DistributionResult()
                            distributionResult.college_id = collegeId
                            distributionResult.student_id = wantStudent.student_id
                            distributionResult.distribution_id = distributionId
                            distributionResult.status = '0'
                            db.session.add(distributionResult)
                            db.session.commit()
                            print('normal: ' + str(wantStudent.student_id) + ' commit ok')
                        else:
                            break
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': distributionNumber,
        'reason': '分配志愿成功！'
    })