from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json

from JSONHelper import JSONHelper
from app import db
from app.models import Student,DistributionDesire,TeacherInfo

'''
    ----------------------------分流志愿-------------------------
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
    查找分流志愿信息
'''