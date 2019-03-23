from flask import jsonify, request, json
from app.api_1_0.sadmin import sadmin
from app.models import ProjectRank
from app import db
from sqlalchemy import or_

'''
    教改项目等级配置
'''

'''
    信息展示
'''
@sadmin.route('/project_rank/get', methods=['GET', 'POST'])
def getProjectrRank():
    projectRanks = ProjectRank.query.all()
    projectRank = ProjectRank.to_json(projectRanks)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': projectRank
    })

'''
    添加
'''
@sadmin.route('/project_rank/add', methods=['GET', 'POST'])
def addProjectRank():
    if request.json['rank_name']:
        projectRank = ProjectRank()
        projectRank.rank_name = request.json['rank_name']
        try:
            db.session.add(projectRank)
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
@sadmin.route('/project_rank/del', methods=['GET', 'POST'])
def delProjectRank():
    projectRank = ProjectRank.query.filter_by(id=request.json['id']).first()
    if projectRank is not None:
        db.session.delete(projectRank)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有此项目类型id'
        })


'''
    更新
'''
@sadmin.route('/project_rank/update', methods=['GET', 'POST'])
def updateProjectRank():
    projectRank = ProjectRank.query.filter_by(id=request.json['id']).first()
    if projectRank is not None:
        projectRank.rank_name = request.json['rank_name']
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
            'reason': '未查询到此项目信息，更新失败'
        })
