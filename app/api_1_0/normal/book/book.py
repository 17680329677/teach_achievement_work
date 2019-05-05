from flask import jsonify, request, json
from app.api_1_0.normal import normal
from app.models import College, TeacherInfo, Book, BookRank
from app import db
from sqlalchemy import or_, and_
from JSONHelper import JSONHelper

'''
获得普通教师出版物的总体信息信息 by request.json['number']=Book.submit_teacher
'''
@normal.route('/book/index', methods=['GET', 'POST'])
def getAllBookInfo():
    book_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'), Book.book_number.label('book_number'),
                                 Book.isbn.label('isbn'), Book.press.label('press'), BookRank.rank_name.label('book_rank'),
                                 Book.status.label('status'), Book.submit_time.label('submit_time'))\
                          .join(BookRank, Book.rank_id == BookRank.id)\
                          .filter(Book.submit_teacher == request.json['number']).all()
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
获得普通教师出版物的所有详细信息 by Book.id
'''
@normal.route('/book/detail', methods=['GET', 'POST'])
def getDetailBookInfo():
    detail_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'), Book.book_number.label('book_number'),
                                   Book.publish_year_month.label('publish_time'), Book.pages.label('pages'), Book.words.label('words'),
                                   Book.isbn.label('isbn'), Book.press.label('press'), Book.version.label('version'), Book.style.label('style'),
                                   BookRank.rank_name.label('rank'), College.name.label('college'), Book.source_project.label('project'),
                                   Book.status.label('status'), Book.cover_path.label('cover_path'), Book.copyright_path.label('copy_path'),
                                   Book.content_path.label('content_path'), Book.participate_teacher.label('authors'),
                                   TeacherInfo.name.label('teacher_name'), Book.submit_time.label('submit_time'))\
                            .join(BookRank, Book.rank_id == BookRank.id)\
                            .join(College, Book.college_id == College.id)\
                            .join(TeacherInfo, Book.submit_teacher == TeacherInfo.number)\
                            .filter(Book.id == request.json['id']).all()

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
    状态更变  [  状态（展示）普通用户角色显示：(1未提交；2已提交；3已存档 ；)    管理员角色显示：(2待审批；3已存档；)   ]
'''

@normal.route('/book/changestatus', methods=['GET', 'POST'])
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
教师删除书籍信息  by Book.id
'''
@normal.route('/book/delete', methods=['GET', 'POST'])
def deleteBookInfo():
    book_info = Book.query.filter_by(id=request.json['id']).first()
    if book_info and book_info.status == '1':
        try:
            db.session.delete(book_info)
            db.session.commit()
            return jsonify({
                'code': 20000,
                'status': 'success'
            })
        except:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '删除失败!'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '删除失败，书籍已提交!'
        })


'''
    修改出版教材信息
'''

@normal.route('/book/submitInfo/change', methods=['GET', 'POST'])
def changeInvigilateSubmitInfo():
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
    cover_path = request.json['cover_path']
    copy_path = request.json['copy_path']
    content_path = request.json['content_path']
    authors = request.json['authors']

    book = Book.query.filter_by(id = id).first()

    if book:
        if book.status == '1':
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
            book.cover_path = cover_path
            book.copyright_path = copy_path
            book.content_path = content_path
            book.participate_teacher = authors
        else:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '教材信息已提交或存档不能修改'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '书籍不存在'
        })

    db.session.commit()
    return jsonify({
        'code': 20000,
        'status': 'success',
        'reason': '修改成功'
    })


'''
根据书籍名称或者书籍状态查询书籍信息 by number
'''
@normal.route('/book/search', methods=['GET', 'POST'])
def searchBookInfo():
    search_type = request.json['search_type']
    search_value = request.json['search_value']
    if search_type == '' and search_value == '':
        book_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'),
                                     Book.book_number.label('book_number'),
                                     Book.isbn.label('isbn'), Book.press.label('press'),
                                     BookRank.rank_name.label('book_rank'),
                                     Book.status.label('status'), Book.submit_time.label('submit_time')) \
            .join(BookRank, Book.rank_id == BookRank.id) \
            .filter(Book.submit_teacher == request.json['number']).all()

    elif search_type == 'book_name':
        book_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'),
                                     Book.book_number.label('book_number'),
                                     Book.isbn.label('isbn'), Book.press.label('press'),
                                     BookRank.rank_name.label('book_rank'),
                                     Book.status.label('status'), Book.submit_time.label('submit_time')) \
            .join(BookRank, Book.rank_id == BookRank.id) \
            .filter(Book.submit_teacher == request.json['number'], Book.book_name.like('%' + search_value + '%')).all()
    elif search_type == 'status':
        book_info = db.session.query(Book.id.label('id'), Book.book_name.label('book_name'),
                                     Book.book_number.label('book_number'),
                                     Book.isbn.label('isbn'), Book.press.label('press'),
                                     BookRank.rank_name.label('book_rank'),
                                     Book.status.label('status'), Book.submit_time.label('submit_time')) \
            .join(BookRank, Book.rank_id == BookRank.id) \
            .filter(Book.submit_teacher == request.json['number'], Book.status.like('%' + search_value + '%')).all()
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
            'reason': 'Found nothing!'
        })