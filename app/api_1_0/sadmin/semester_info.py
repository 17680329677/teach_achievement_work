from flask import jsonify, request, json
from app.api_1_0.sadmin import sadmin
from app.models import SemesterInfo
from app import db
from sqlalchemy import or_

'''
    学期配置 
    
    注意事项：
'''

'''
    信息展示
'''
@sadmin.route('/semester_info/get', methods=['GET', 'POST'])
def getSemesterInfo():
    semesterInfos = SemesterInfo.query.all()
    semesterInfo = SemesterInfo.to_json(semesterInfos)
    return jsonify({
        'code': 20000,
        'status': 'success',
        'data': semesterInfo
    })

'''
    添加
'''
@sadmin.route('/semester_info/add', methods=['GET', 'POST'])
def addSemesterInfo():
    if request.json['semester_name'] is not None and request.json['status'] is not None :
        semesterInfo = SemesterInfo()
        semesterInfo.semester_name = request.json['semester_name']
        semesterInfo.status = request.json['status']
        try:
            db.session.add(semesterInfo)
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
@sadmin.route('/semester_info/del', methods=['GET', 'POST'])
def delSemesterInfo():
    semesterInfo = SemesterInfo.query.filter_by(id=request.json['id']).first()
    if semesterInfo is not None:
        db.session.delete(semesterInfo)
        db.session.commit()
        return jsonify({
            'code': 20000,
            'status': 'success'
        })
    else:
        return jsonify({
            'code': 20001,
            'status': 'failed',
            'reason': '没有此学期信息id'
        })


'''
    更新
'''
@sadmin.route('/semester_info/update', methods=['GET', 'POST'])
def updateSemesterInfo():
    semesterInfo = SemesterInfo.query.filter_by(id=request.json['id']).first()
    if semesterInfo is not None:
        semesterInfo.semester_name = request.json['semester_name']
        semesterInfo.status = request.json['status']
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
            'reason': '未查询到此学期信息，更新失败'
        })
