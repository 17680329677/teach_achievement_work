from flask import jsonify, request, json
from app.api_1_0.cadmin import cadmin
from sqlalchemy import or_
import json
from werkzeug.security import generate_password_hash

from app import db
from app.models import TeacherInfo,Book,BookRank,College,TeacherBook
from JSONHelper import JSONHelper

'''
    教师出版书籍
'''

'''
    获得本学院 图书总体信息 by token 并且状态 status ！= 1
'''
@cadmin.route('/book/index', methods=['GET', 'POST'])
def getAllBookInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id


    book_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'), Book.book_number.label('book_number'),
                                 Book.isbn.label('isbn'), Book.press.label('press'), BookRank.rank_name.label('book_rank'),
                                 Book.status.label('status'), Book.submit_time.label('submit_time'))\
                          .join(BookRank, Book.rank_id == BookRank.id)\
                          .filter(Book.college_id == collegeId,  Book.status != 1 ).all()
    if book_info:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(book_info)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'something was wrong!'
        })

'''
    获得某个图书的详细信息 by Book.id
'''
@cadmin.route('/book/detail', methods=['GET', 'POST'])
def getDetailBookInfo():
    bookId = request.json['id']
    detail_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'), Book.book_number.label('book_number'),
                                   Book.publish_year_month.label('publish_time'), Book.pages.label('pages'), Book.words.label('words'),
                                   Book.isbn.label('isbn'), Book.press.label('press'), Book.version.label('version'), Book.style.label('style'),
                                   BookRank.id.label('rank_id'), College.name.label('college'), Book.source_project.label('project'),
                                   Book.status.label('status'), Book.cover_path.label('cover_path'), Book.copyright_path.label('copy_path'),
                                   Book.content_path.label('content_path'), Book.participate_teacher.label('authors'),
                                   TeacherInfo.name.label('teacher_name'), Book.submit_time.label('submit_time'))\
                            .join(BookRank, Book.rank_id == BookRank.id)\
                            .join(College, Book.college_id == College.id)\
                            .join(TeacherInfo, Book.submit_teacher == TeacherInfo.number)\
                            .filter(Book.id == bookId).all()

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
    修改图书信息
'''

@cadmin.route('/book/submitInfo/change', methods=['GET', 'POST'])
def changeSubmitInfo():
    id = request.json['id']
    book_name = request.json['book_name']
    book_number = request.json['book_number']
    publish_time = request.json['publish_time']
    pages = request.json['pages']
    words = request.json['words']
    isbn = request.json['isbn']
    press = request.json['press']
    version = request.json['version']
    style = request.json['style']
    rank_id = request.json['rank_id']
    project = request.json['project']
    status = request.json['status']
    cover_path = request.json['cover_path']
    copy_path = request.json['copy_path']
    content_path = request.json['content_path']
    authors = request.json['authors']

    book = Book.query.filter_by(id = id).first()
    book.id = id
    book.book_name = book_name
    book.book_number = book_number
    book.publish_year_month = publish_time
    book.pages = pages
    book.words = words
    book.isbn = isbn
    book.press = press
    book.version = version
    book.style = style
    book.rank_id = rank_id
    book.source_project = project
    book.status = status
    book.cover_path = cover_path
    book.copyright_path = copy_path
    book.content_path = content_path
    book.participate_teacher = authors

    db.session.commit()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': ''
    })

'''
    状态更变  [  状态（展示）普通用户角色显示：(1未提交；2已提交；3已存档 ；)    管理员角色显示：(2待审批；3已存档；)   ]
'''

@cadmin.route('/book/changestatus', methods=['GET', 'POST'])
def changeBookStatus():
    id = request.json['id']
    status = request.json['status']
    book_info = Book.query.filter_by(id = id).first()
    if book_info:
        try:
            book_info.status = status
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
    搜索
    根据书籍名称或者书籍状态查询书籍信息 by number   并且状态不为待提交
'''
@cadmin.route('/book/search', methods=['GET', 'POST'])
def searchBookInfo():
    cadminToken = request.json['token']  # token 是管理员的工号
    cadminInfo = TeacherInfo.query.filter_by(number=cadminToken).first()
    collegeId = cadminInfo.college_id

    search_type = request.json['search_type']
    search_value = request.json['search_value']
    if search_type == '' and search_value == '':
        book_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'),
                                     Book.book_number.label('book_number'),
                                     Book.isbn.label('isbn'), Book.press.label('press'),
                                     BookRank.rank_name.label('book_rank'),
                                     Book.status.label('status'), Book.submit_time.label('submit_time')) \
            .join(BookRank, Book.rank_id == BookRank.id) \
            .filter(Book.college_id == collegeId, Book.status != 1).all()

    elif search_type == 'book_name':
        book_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'),
                                     Book.book_number.label('book_number'),
                                     Book.isbn.label('isbn'), Book.press.label('press'),
                                     BookRank.rank_name.label('book_rank'),
                                     Book.status.label('status'), Book.submit_time.label('submit_time')) \
            .join(BookRank, Book.rank_id == BookRank.id) \
            .filter(Book.college_id == collegeId, Book.book_name.like('%' + search_value + '%'), Book.status != 1).all()
    elif search_type == 'status':
        book_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'),
                                     Book.book_number.label('book_number'),
                                     Book.isbn.label('isbn'), Book.press.label('press'),
                                     BookRank.rank_name.label('book_rank'),
                                     Book.status.label('status'), Book.submit_time.label('submit_time')) \
            .join(BookRank, Book.rank_id == BookRank.id) \
            .filter(Book.college_id == collegeId, Book.status.like('%' + search_value + '%'), Book.status != 1).all()
    elif search_type == 'teacher_number':
        book_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'),
                                     Book.book_number.label('book_number'),
                                     Book.isbn.label('isbn'), Book.press.label('press'),
                                     BookRank.rank_name.label('book_rank'),
                                     Book.status.label('status'), Book.submit_time.label('submit_time')) \
            .join(BookRank, Book.rank_id == BookRank.id) \
            .filter(Book.college_id == collegeId, Book.submit_teacher.like('%' + search_value + '%'), Book.status != 1).all()
    elif search_type == '' and search_value != '':
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': 'please selected search type!'
        })
    if book_info:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': JSONHelper.jsonBQlist(book_info)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有匹配的书籍!'
        })