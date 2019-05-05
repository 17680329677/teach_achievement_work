from flask import jsonify, request
from app.api_1_0.cadmin import cadmin

from app import db
from app.models import TeacherInfo,College,TeacherPaper,TeachReformPaper
from JSONHelper import JSONHelper

'''
    教改论文
'''

'''
    获得本学院 论文总体信息 by token 并且状态 status ！= 1
'''
@cadmin.route('/reform_paper/index', methods=['GET', 'POST'])
def getAllReformPaperInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    teachReformPaper = db.session.query(    TeachReformPaper.id.label('id'),\
                                            TeachReformPaper.paper_name.label('paper_name'),\
                                            TeachReformPaper.paper_number.label('paper_number'), \
                                            TeacherInfo.name.label('teacher_name'),\
                                            TeachReformPaper.status.label('status'),\
                                            TeachReformPaper.publish_year_month.label('publish_year_month')\
                                 )\
        .join(TeacherPaper, TeacherPaper.paper_id == TeachReformPaper.id) \
        .join(TeacherInfo, TeacherInfo.number == TeacherPaper.teacher_number) \
        .filter(TeachReformPaper.college_id == collegeId,  TeachReformPaper.status != '1' ).all()
    if teachReformPaper:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(teachReformPaper)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有论文!'
        })

'''
    获得某个论文的详细信息 by .id
'''
@cadmin.route('/reform_paper/detail', methods=['GET', 'POST'])
def getDetailReformPaperInfo():
    paperId = request.json['id']
    detail_info = db.session.query(
                                    TeachReformPaper.id.label('id') ,\

                                    TeacherInfo.number.label('teacher_number'),\
                                    TeacherInfo.name.label('teacher_name'),\
                                    TeacherPaper.order.label('order'),\

                                    TeachReformPaper.paper_name.label('paper_name') ,\
                                    TeachReformPaper.paper_number.label('paper_number') ,\
                                    TeachReformPaper.journal_name.label('journal_name') ,\
                                    TeachReformPaper.publish_year_month.label('publish_year_month') ,\
                                    TeachReformPaper.journal_year.label('journal_year') ,\
                                    TeachReformPaper.journal_number.label('journal_number') ,\
                                    TeachReformPaper.college_id.label('college_id') ,\
                                    TeachReformPaper.journal_volum.label('journal_volum') ,\
                                    TeachReformPaper.status.label('status') ,\
                                    TeachReformPaper.source_project.label('source_project') ,\
                                    TeachReformPaper.cover_path.label('cover_path') ,\
                                    TeachReformPaper.content_path.label('content_path') ,\
                                    TeachReformPaper.text_path.label('text_path') ,\
                                    TeachReformPaper.cnki_url.label('cnki_url') ,\
                                    TeachReformPaper.participate_teacher.label('participate_teacher') ,\
                                   ) \
        .join(TeacherPaper, TeacherPaper.paper_id == TeachReformPaper.id) \
        .join(TeacherInfo, TeacherInfo.number == TeacherPaper.teacher_number) \
        .filter(TeachReformPaper.id == paperId).all()

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
            'reason': '信息为空!'
        })

'''
    修改论文信息
'''
@cadmin.route('/reform_paper/submitInfo/change', methods=['GET', 'POST'])
def changeReformPaperSubmitInfo():
    id = request.json['id']

    order = request.json['order']
    paper_name = request.json['paper_name']
    paper_number = request.json['paper_number']
    journal_name = request.json['journal_name']
    publish_year_month = request.json['publish_year_month']
    journal_year = request.json['journal_year']
    journal_number = request.json['journal_number']
    #college_id = request.json['college_id']
    journal_volum = request.json['journal_volum']
    #status = request.json['status']
    source_project = request.json['source_project']
    cover_path = request.json['cover_path']
    content_path = request.json['content_path']
    text_path = request.json['text_path']
    cnki_url = request.json['cnki_url']
    participate_teacher = request.json['participate_teacher']

    teachReformPaper = TeachReformPaper.query.filter_by(id = id).first()
    teacherPaper = TeacherPaper.query.filter_by(paper_id = id).first()

    teacherPaper.order = order
    teachReformPaper.paper_name = paper_name
    teachReformPaper.paper_number = paper_number
    teachReformPaper.journal_name = journal_name
    teachReformPaper.publish_year_month = publish_year_month
    teachReformPaper.journal_year = journal_year
    teachReformPaper.journal_number = journal_number
    #teachReformPaper.college_id = college_id
    teachReformPaper.journal_volum = journal_volum
    #teachReformPaper.status = status
    teachReformPaper.source_project = source_project
    teachReformPaper.cover_path = cover_path
    teachReformPaper.content_path = content_path
    teachReformPaper.text_path = text_path
    teachReformPaper.cnki_url = cnki_url
    teachReformPaper.participate_teacher = participate_teacher

    db.session.commit()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': ''
    })

'''
    论文状态更变  [  （1未提交、2提交/待审核、3存档/已审核）   ]
'''
@cadmin.route('/reform_paper/changestatus', methods=['GET', 'POST'])
def reformPaperChangeStatus():
    id = request.json['id']
    status = request.json['status']
    reformPaper = TeachReformPaper.query.filter_by(id=id).first()
    if reformPaper:
        try:
            reformPaper.status = status
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
            'reason': '没有匹配的项目'
        })


'''
    按状态搜索： 
    status：状态：1未提交、2提交/待审核、3存档/已审核   ps：0全部搜索
'''
@cadmin.route('/reform_paper/status_search', methods=['GET', 'POST'])
def statusSearchReformPaper():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    status = request.json['status']

    teachReformPapers = db.session.query(   TeachReformPaper.id.label('id'),\
                                            TeachReformPaper.paper_name.label('paper_name'),\
                                            TeachReformPaper.paper_number.label('paper_number'),\
                                            TeacherInfo.name.label('teacher_name'),\
                                            TeachReformPaper.status.label('status'),\
                                            TeachReformPaper.publish_year_month.label('publish_year_month')\
                                    )\
        .join(TeacherPaper, TeacherPaper.paper_id == TeachReformPaper.id) \
        .join(TeacherInfo, TeacherInfo.number == TeacherPaper.teacher_number)
    if status != '0':
        teachReformPapers = teachReformPapers.filter(TeachReformPaper.college_id == collegeId,  TeachReformPaper.status == status )
    else:
        teachReformPapers = teachReformPapers.filter(TeachReformPaper.college_id == collegeId)

    teachReformPaper = teachReformPapers.order_by(TeachReformPaper.publish_year_month.desc()).all()
    if teachReformPaper:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(teachReformPaper)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有匹配项目!'
        })

'''
    按教改论文姓名和教师姓名搜索
    根据 查询项目信息 by number   并且状态不为待提交
'''

@cadmin.route('/reform_paper/search', methods=['GET', 'POST'])
def searchReformPaperInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    search_type = request.json['search_type']
    search_value = request.json['search_value']
    teachReforms = db.session.query(        TeachReformPaper.id.label('id'),\
                                            TeachReformPaper.paper_name.label('paper_name'),\
                                            TeachReformPaper.paper_number.label('paper_number'), \
                                            TeacherInfo.name.label('teacher_name'),\
                                            TeachReformPaper.status.label('status'),\
                                            TeachReformPaper.publish_year_month.label('publish_year_month')\
                                    )\
        .join(TeacherPaper, TeacherPaper.paper_id == TeachReformPaper.id) \
        .join(TeacherInfo, TeacherInfo.number == TeacherPaper.teacher_number)

    if search_type == '' and search_value == '':
        teachReforms = teachReforms.filter(TeachReformPaper.college_id == collegeId,
                                          TeachReformPaper.status != '1')

    elif search_type == 'reform_name':
        teachReforms = teachReforms \
            .filter(TeachReformPaper.college_id == collegeId,
                    TeachReformPaper.paper_name.like('%' + search_value + '%'), TeachReformPaper.status != '1')

    elif search_type == 'teacher_name':
        teachReforms = teachReforms \
            .filter(TeachReformPaper.college_id == collegeId, TeacherInfo.name.like('%' + search_value + '%'),
                    TeachReformPaper.status != '1')

    elif search_type == '' and search_value != '':
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'please selected search type!'
        })

    teachReform = teachReforms.order_by(TeachReformPaper.publish_year_month.desc()).all()
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
            'reason': '没有匹配到该论文!'
        })