from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json
from werkzeug.security import generate_password_hash
from sqlalchemy.orm import aliased

from app import db
from app.models import Department,TeacherInfo,TeacherType,Teacher,College,TeacherTitle,TeacherCategory
from JSONHelper import JSONHelper

'''
    教师信息管理
'''


'''
    返回本院的所有教师信息
'''
@cadmin.route('/teacher_info/get',methods=['GET','POST'])
def getTeacherInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    #SQLAlchemy 使用 aliased() 方法表示别名,当我们需要把同一张表连接多次的时候，常常需要用到别名
    TeachTitle = aliased(TeacherTitle)
    ManageTitle = aliased(TeacherTitle)

    teacherInfo = db.session.query(
        TeacherInfo.id,
        TeacherInfo.number,
        TeacherInfo.name,
        TeacherInfo.gender,
        TeacherInfo.nationality,
        TeacherInfo.birth_year_month,
        TeacherInfo.college_id,
        College.name.label('college_name'),
        TeacherInfo.department_id,
        Department.name.label('department_name'),
        TeacherInfo.teachertitle_id,
        TeachTitle.name.label('teachertitle_name'),
        TeacherInfo.managertitle_id,
        ManageTitle.name.label('managertitle_name'),
        TeacherInfo.teacher_category_id,
        TeacherCategory.name.label('teacher_category_name'),
        TeacherInfo.type,
        TeacherInfo.type_id,
        TeacherInfo.work_begin_year_month,
        TeacherInfo.bjfu_join_year_month,
        TeacherInfo.highest_education,
        TeacherInfo.highest_education_accord_year_month,
        TeacherInfo.graduate_paper_title,
        TeacherInfo.graduate_school,
        TeacherInfo.research_direction,
        TeacherInfo.telephone,
        TeacherInfo.email,
        TeacherInfo.status
    )\
        .join(TeacherCategory, TeacherCategory.id == TeacherInfo.teacher_category_id) \
        .join(TeachTitle , TeachTitle.id == TeacherInfo.teachertitle_id) \
        .join(ManageTitle , ManageTitle.id == TeacherInfo.managertitle_id )\
        .join(Department, Department.id == TeacherInfo.department_id )\
        .join(College, College.id == TeacherInfo.college_id)\
        .filter(TeacherInfo.college_id == collegeId, TeacherInfo.type_id == 5).all()

    teacherInfo = JSONHelper.jsonBQlist(teacherInfo)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': teacherInfo
    })

'''
    新增教师信息
    默认教师密码： 123456
'''
@cadmin.route('/teacher_info/add',methods=['GET','POST'])
def addTeacherInfo():
    '''
    test = request.json['test']
    print(isinstance(request.json['test'],int))
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': ''
    })
    '''


    errState = 0
    errMessage = ''

    number = request.json['number']
    if not number:
        errState = 1
        errMessage = '教师工号未填写'
    name = request.json['name']
    if not name:
        errState = 1
        errMessage = '教师姓名未填写'
    gender = request.json['gender']
    if not gender:
        errState = 1
        errMessage = '教师性别未填写'
    nationality = request.json['nationality']  #民族
    birth_year_month = request.json['birth_year_month']


    '''---------------department_id--------------'''
    department_id = None
    if isinstance(request.json['department_id'], int) or not request.json['department_id']:
        department_id = request.json['department_id'] #  //如果导入信息的化可以直接填写  所属教研室id，
        if not department_id:
            department_id = 0 #如果没有 初始化默认为0，表示未分配,等待学院管理员分配
    else:
        department = Department.query.filter(Department.name.like('%' + request.json['department_id'] + '%')).first()
        if department:
            department_id = department.id

    '''----------------college_id-------------'''
    college_id = None
    if isinstance(request.json['college_id'], int) or not request.json['college_id']:
        college_id = request.json['college_id'] #  //如果导入信息的化可以直接填写  所属教研室id，
        if not college_id:
            #pass  # college_id = 0 #如果没有 初始化默认为0，表示未分配
            errState = 1
            errMessage = '所属学院未填写'
    else:
        college = College.query.filter( College.name.like('%' + request.json['college_id'] + '%') ).first()
        if college:
            college_id = college.id

    '''----------------teachertitle_id-------------'''
    teachertitle_id = None
    if isinstance(request.json['teachertitle_id'], int) or not request.json['teachertitle_id']:
        teachertitle_id = request.json['teachertitle_id'] #  //如果导入信息的化可以直接填写  所属教研室id，
        if not teachertitle_id:
            pass
    else:
        teacherTitle = TeacherTitle.query.filter( TeacherTitle.name.like('%' + request.json['teachertitle_id'] + '%') ).first()
        if teacherTitle:
            teachertitle_id = teacherTitle.id

    '''----------------managertitle_id-------------'''
    managertitle_id = None
    if isinstance(request.json['managertitle_id'], int) or not request.json['teachertitle_id']:
        teachertitle_id = request.json['managertitle_id'] #  //如果导入信息的化可以直接填写  所属教研室id，
        if not teachertitle_id:
            pass
    else:
        managerTitle = TeacherTitle.query.filter( TeacherTitle.name.like('%' + request.json['managertitle_id'] + '%') ).first()
        if managerTitle:
            teachertitle_id = managerTitle.id

    '''---------------teacher_category_id--------------'''
    teacher_category_id = None
    if isinstance(request.json['teacher_category_id'], int) or not request.json['teacher_category_id']:
        teacher_category_id = request.json['teacher_category_id']  # //如果导入信息的化可以直接填写  所属教研室id，
        if not teacher_category_id:
            errState = 1
            errMessage = '教师类型未填写'
    else:
        teacherCategory = TeacherCategory.query.filter(TeacherCategory.name.like('%' + request.json['teacher_category_id'] + '%')).first()
        if teacherCategory:
            teacher_category_id = teacherCategory.id

    '''---------------【教师类型信息自动判断】如果教师类型信息 上传数据中没有，首先根据根据教学职称的父类自动补充，其次根据管理职称职称的父类自动补充--------------'''
    if not teacher_category_id:
        if teachertitle_id or managertitle_id:
            if managertitle_id:
                teacher_category_id = TeacherTitle.query.filter_by(id = managertitle_id).first()
            if teachertitle_id:
                teacher_category_id = TeacherTitle.query.filter_by(id = teachertitle_id).first()

    type = request.json['type']
    '''---------------【双肩挑信息自动判断】--------------'''
    if teachertitle_id and managertitle_id:
        type = "是"

    normalId = TeacherType.query.filter_by(role = 'normal').first().id
    type_id = normalId #指向teacher_type表的id

    status = request.json['status']
    work_begin_year_month = request.json['work_begin_year_month']
    bjfu_join_year_month = request.json['bjfu_join_year_month']
    highest_education = request.json['highest_education']
    highest_education_accord_year_month = request.json['highest_education_accord_year_month']
    graduate_paper_title = request.json['graduate_paper_title']
    graduate_school = request.json['graduate_school']
    research_direction = request.json['research_direction']
    telephone = request.json['telephone']
    email = request.json['email']

    teacher = TeacherInfo.query.filter_by(number=number).first()
    if teacher:
        errState = 1
        errMessage = teacher.name + '('+str(number)+')' +' 此教师已存在'

    # 出现错误
    if errState:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': errMessage
        })

    #向teacher表中写入数据
    teacher = Teacher()
    teacher.number = number
    teacher.password = generate_password_hash('123456')
    teacher.type = 5

    #向teacher_info中分配写入数据:
    teacherInfo = TeacherInfo()
    teacherInfo.number = number
    teacherInfo.name = name
    teacherInfo.gender = gender
    teacherInfo.nationality = nationality
    teacherInfo.birth_year_month = birth_year_month
    teacherInfo.department_id = department_id
    teacherInfo.college_id = college_id
    teacherInfo.teachertitle_id = teachertitle_id
    teacherInfo.managertitle_id = managertitle_id
    teacherInfo.teacher_category_id = teacher_category_id
    teacherInfo.type = type
    teacherInfo.type_id = type_id
    teacherInfo.status = status
    teacherInfo.work_begin_year_month = work_begin_year_month
    teacherInfo.bjfu_join_year_month = bjfu_join_year_month
    teacherInfo.highest_education = highest_education
    teacherInfo.highest_education_accord_year_month = highest_education_accord_year_month
    teacherInfo.graduate_paper_title = graduate_paper_title
    teacherInfo.graduate_school = graduate_school
    teacherInfo.research_direction = research_direction
    teacherInfo.telephone = telephone
    teacherInfo.email = email

    try:
        db.session.add(teacher) #向teacher表中提交信息
        db.session.add(teacherInfo) #向teacher_info表中提交信息
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '添加成功！'
        })
    except:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '保存失败！'
        })

'''
    删除教师有关信息（功能保留）
'''
@cadmin.route('/teacher_info/del',methods=['GET','POST'])
def delTeacherInfo():
    number = request.json['number']
    teacher = Teacher.query.filter_by(number = number).first()
    teacherInfo = TeacherInfo.query.filter_by(number = number).first()
    #db.session.delete(teacher)
    #db.session.delete(teacherInfo)
    try:
        #db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '删除成功！'
        })
    except:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '删除失败！'
        })

'''
    修改教师信息  by number 教师工号
'''
@cadmin.route('/teacher_info/update',methods=['GET','POST'])
def updateTeacherInfo():
    errState = 0
    errMessage = ''

    number = request.json['number']
    if not number:
        errState = 1
        errMessage = '教师工号未填写'

    teacherInfo = TeacherInfo.query.filter_by(number=number).first()

    # 修改项：
    name = request.json['name']
    if not name:
        errState = 1
        errMessage = '教师姓名未填写'
    gender = request.json['gender']
    if not gender:
        errState = 1
        errMessage = '教师性别未填写'
    nationality = request.json['nationality']  # 民族
    birth_year_month = request.json['birth_year_month']
    department_id = request.json['department_id']  # 所属教研室id，初始化默认为0，表示未分配,等待学院管理员分配
    college_id = request.json['college_id']  # 外校教师可以没有
    if not college_id:
        errState = 1
        errMessage = '所属学院未填写'
    teachertitle_id = request.json['teachertitle_id']
    managertitle_id = request.json['managertitle_id']
    type = request.json['type']

    normalId = TeacherType.query.filter_by(role='normal').first().id
    type_id = normalId  # 指向teacher_type表的id

    status = request.json['status']
    work_begin_year_month = request.json['work_begin_year_month']
    bjfu_join_year_month = request.json['bjfu_join_year_month']
    highest_education = request.json['highest_education']
    highest_education_accord_year_month = request.json['highest_education_accord_year_month']
    graduate_paper_title = request.json['graduate_paper_title']
    graduate_school = request.json['graduate_school']
    research_direction = request.json['research_direction']
    telephone = request.json['telephone']
    email = request.json['email']

    # 分配写入数据:
    teacherInfo.number = number
    teacherInfo.name = name
    teacherInfo.gender = gender
    teacherInfo.nationality = nationality
    teacherInfo.birth_year_month = birth_year_month
    teacherInfo.department_id = department_id
    teacherInfo.college_id = college_id
    teacherInfo.teachertitle_id = teachertitle_id
    teacherInfo.managertitle_id = managertitle_id
    teacherInfo.type = type
    teacherInfo.type_id = type_id
    teacherInfo.status = status
    teacherInfo.work_begin_year_month = work_begin_year_month
    teacherInfo.bjfu_join_year_month = bjfu_join_year_month
    teacherInfo.highest_education = highest_education
    teacherInfo.highest_education_accord_year_month = highest_education_accord_year_month
    teacherInfo.graduate_paper_title = graduate_paper_title
    teacherInfo.graduate_school = graduate_school
    teacherInfo.research_direction = research_direction
    teacherInfo.telephone = telephone
    teacherInfo.email = email

    #出现错误
    if errState:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': errMessage
        })

    try:
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '更新成功！'
        })
    except:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '更新失败！'
        })