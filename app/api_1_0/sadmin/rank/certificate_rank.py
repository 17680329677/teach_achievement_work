from flask import jsonify, request
from app.api_1_0.sadmin import sadmin
from app.models import CertificateRank
from app import db

'''
    CertificateRank  证书等级列表  增删改查
'''

'''
    展示所有证书等级
'''
@sadmin.route('/certificate_rank/index', methods=['GET', 'POST'])
def getCertificateRankInfo():
    certificateRank = CertificateRank.query.all()
    if certificateRank:
        return jsonify({
            'code': 20000,
            'status': 'success',
            'data': CertificateRank.to_json(certificateRank)
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有查询到信息！'
        })

'''
    添加证书等级 
'''
@sadmin.route('/certificate_rank/add', methods=['GET', 'POST'])
def addCertificateRankInfo():
    rankInfo = CertificateRank.query.filter_by(rank_name = request.json['rank_name']).first()
    if rankInfo:
        return jsonify({
            'code':20001,
            'status': 'failed',
            'reason': '名称重复'
        })
    else:
        certificateRank = CertificateRank()
        certificateRank.rank_name = request.json['rank_name']
        try:
            db.session.add(certificateRank)
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

'''
    删除证书等级信息
'''
@sadmin.route('/certificate_rank/del', methods=['GET', 'POST'])
def delCertificateRankInfo():
    rankInfo = CertificateRank.query.filter_by(id = request.json['id']).first()
    if rankInfo:
        db.session.delete(rankInfo)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '证书等级信息不存在！'
        })

'''
    修改证书等级信息
'''
@sadmin.route('/certificate_rank/update', methods=['GET', 'POST'])
def updateCertificateRankInfo():
    rankInfo = CertificateRank.query.filter_by(id = request.json['id']).first()
    if rankInfo is not None:
        rankInfo.id = request.json['id']
        rankInfo.rank_name = request.json['rank_name']
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