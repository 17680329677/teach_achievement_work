from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json

from JSONHelper import JSONHelper
from app import db
from app.models import Student,TeacherInfo

'''
        学生信息导入
'''

'''
    查看当前学院所有学生
'''
@cadmin.route('/students_info/get',methods=['GET','POST'])
def getStudentInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    students = Student.query.filter_by(college_id=collegeId).all()
    students = Student.to_json(students)
    for stu in students:
        del stu['password']

    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': students
    })
