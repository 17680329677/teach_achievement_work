from flask import jsonify, request, json
from app.api_1_0.normal import normal
from app.models import College, TeacherInfo, Book, BookRank
from app import db
from sqlalchemy import or_, and_
from JSONHelper import JSONHelper


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


@normal.route('/book/changestatus/submit', methods=['GET', 'POST'])
def changeToSubmit():
    book_info = Book.query.filter_by(id=request.json['id']).first()
    if book_info:
        try:
            book_info.status = '已提交'
            db.session.commit()
            return jsonify({
                'code': 20000,
                'status': 'success'
            })
        except:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '提交失败!'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '提交失败!'
        })


@normal.route('/book/changestatus/recallsubmit', methods=['GET', 'POST'])
def recallSubmit():
    book_info = Book.query.filter_by(id=request.json['id']).first()
    if book_info:
        try:
            book_info.status = '未提交'
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


@normal.route('/book/delete', methods=['GET', 'POST'])
def deleteBookInfo():
    book_info = Book.query.filter_by(id=request.json['id']).first()
    if book_info:
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
            'reason': '删除失败!'
        })


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