from flask import jsonify, request, json
from app.api_1_0.sadmin import sadmin
from app.models import InnovationRank
from app import db
from sqlalchemy import or_

'''
    大创等级配置
'''

'''
    信息展示
'''
@sadmin.route('/innovation_rank/get', methods=['GET', 'POST'])
def getInnovationRank():
    innovationRanks = InnovationRank.query.all()
    innovationRank = InnovationRank.to_json(innovationRanks)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': innovationRank
    })

'''
    添加
'''
@sadmin.route('/innovation_rank/add', methods=['GET', 'POST'])
def addInnovationRank():
    if request.json['rank_name'] is not None:
        innovationRank = InnovationRank()
        innovationRank.rank_name = request.json['rank_name']
        try:
            db.session.add(innovationRank)
            db.session.commit()
            return jsonify({
                'code':20000,
                'status': 'success'
            })
        except:
            return jsonify({
                'code': 20001,
                'status': 'failed',
                'reason': '保存失败！'
            })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '信息不完整'
        })

'''
    删除
'''
@sadmin.route('/innovation_rank/del', methods=['GET', 'POST'])
def delInnovationRank():
    innovationRank = InnovationRank.query.filter_by(id=request.json['id']).first()
    if innovationRank is not None:
        db.session.delete(innovationRank)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有等级配置id'
        })


'''
    更新
'''
@sadmin.route('/innovation_rank/update', methods=['GET', 'POST'])
def updateInnovationRank():
    innovationRank = InnovationRank.query.filter_by(id=request.json['id']).first()
    if innovationRank is not None:
        innovationRank.rank_name = request.json['rank_name']
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success',
            'reason': '信息更新成功'
        })
    else:
        return jsonify({
            'code': 20000,
            'status': 'failed',
            'reason': '未查询到此等级配置信息，更新失败'
        })
