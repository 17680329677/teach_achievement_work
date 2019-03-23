from flask import jsonify, request
from app.api_1_0.sadmin import sadmin
from app.models import BookRank
from app import db

'''
    BookRank  教材级别表  例如：国家级精品教材等。
'''

'''
    展示 教材级别信息
'''
@sadmin.route('/bookrank/index', methods=['GET', 'POST'])
def getBookRankInfo():
    book_rank_info = BookRank.query.all()
    if book_rank_info:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': BookRank.to_json(book_rank_info)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有查询到信息！'
        })

'''
    交材级别信息更新 by book_rank.id
'''
@sadmin.route('/bookrank/update', methods=['GET', 'POST'])
def updateBookRankInfo():
    id = request.json['id']
    rank_name = request.json['rank_name']
    rank_info = BookRank.query.filter_by(id=id).first()
    if rank_info:
        rank_info.rank_name = rank_name
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '修改失败！'
        })

'''
    添加交材级别信息
'''
@sadmin.route('/bookrank/add', methods=['GET', 'POST'])
def addBookRankInfo():
    rank_info = BookRank.query.filter_by(rank_name = request.json['rank_name']).first()
    if rank_info:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '名称重复！'
        })
    else:
        book_rank = BookRank()
        book_rank.rank_name = request.json['rank_name']
        try:
            db.session.add(book_rank)
            db.session.commit()
            return jsonify({
                'code': 20000,
                'status': 'success'
            })
        except:
            return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '保存失败！'
        })

'''
    删除交材级别信息
'''
@sadmin.route('/bookrank/delete', methods=['GET', 'POST'])
def deleteBookRankInfo():
    book_rank = BookRank.query.filter_by(id=request.json['id']).first()
    if book_rank:
        db.session.delete(book_rank)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '等级信息不存在！'
        })
