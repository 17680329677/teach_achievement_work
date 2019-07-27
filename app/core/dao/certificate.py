from app import db
from werkzeug.security import check_password_hash
#from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
#from flask import current_app



from sqlalchemy import Column, DateTime, Float, ForeignKey, String, Boolean, Date
from sqlalchemy.dialects.mysql import INTEGER,BIGINT
from sqlalchemy.orm import relationship
# from sqlalchemy.ext.declarative import declarative_base

from app.utils.url_condition.url_condition_mysql import UrlCondition, process_query, count_query, page_query
from app.utils.Error import CustomError
from datetime import datetime

class CertificateInfo(db.Model):
    __tablename__ = 'certificate_info'

    id = Column(INTEGER(11), primary_key=True)
    certificate_name = Column(String(255),default='' )
    ranking = Column(String(50),default='' )
    rank_id = Column(INTEGER(11),default=0  )
    organize_unit = Column(String(255),default='' )
    teacher_number = Column(String(80),default='' )
    grant_time = Column(Date, default=datetime.now )
    project_id = Column(INTEGER(11),default=0 )
    type = Column(String(60),default='')
    certificate_pic_path = Column(String(255),default='')
    status = Column(String(255),default='' )
    college_id = Column(INTEGER(11),default=0 )
    participate_student = Column(String(255),default='')
    submit_time = Column(Date, default=datetime.now )
    using = Column(Boolean,default=True )

    @classmethod
    def reformatter_insert(cls, data: dict):
        '''
        插入之前格式化
        :param data: dict  要格式化的dict字典
        :return: dict 格式化后的dict字典
        '''
        return data

    @classmethod
    def reformatter_update(cls, data: dict):
        '''
        更新之格式化
        :param data: dict  要格式化的dict类
        :return: dict 格式化后的dict类
        '''
        return data

    @classmethod
    def formatter(cls, certificate_info):
        '''
        数据格式化
        :param certificate_info: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if certificate_info is None:
            return None
        try:
            certificate_info_dict = {
                'id' :certificate_info.id,
                'certificate_name' :certificate_info.certificate_name,
                'ranking' :certificate_info.ranking,
                'rank_id' :certificate_info.rank_id,
                'organize_unit' :certificate_info.organize_unit,
                'teacher_number' :certificate_info.teacher_number,
                'grant_time' :certificate_info.grant_time,
                'project_id' :certificate_info.project_id,
                'type' :certificate_info.type,
                'certificate_pic_path' :certificate_info.certificate_pic_path,
                'status' :certificate_info.status,
                'college_id' :certificate_info.college_id,
                'participate_student' :certificate_info.participate_student,
                'submit_time' :certificate_info.submit_time
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return certificate_info_dict

    @classmethod
    def count(cls, query_dict: dict, unscoped: bool = False):
        '''
        计数
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: total int 查询数量的结果
        '''
        if query_dict is None:
            query_dict = {}
        query = CertificateInfo.query
        if not unscoped:
            query = query.filter(CertificateInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, CertificateInfo)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_certificate_info(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        certificate_info = CertificateInfo()
        for key, value in data.items():
            if hasattr(CertificateInfo, key):
                setattr(certificate_info, key, value)
        db.session.add(certificate_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_certificate_info(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        certificate_info = CertificateInfo.query
        if not unscoped:
            certificate_info = certificate_info.filter(CertificateInfo.using == True)
        try:
            certificate_info = certificate_info.filter(CertificateInfo.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(certificate_info)

    @classmethod
    def query_certificate_info(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = CertificateInfo.query
        if not unscoped:
            query = query.filter(CertificateInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, CertificateInfo)
            (certificate_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(certificate_info) for certificate_info in certificate_infos], total

    @classmethod
    def delete_certificate_info(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = CertificateInfo.query.filter(CertificateInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, CertificateInfo)
            (certificate_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for certificate_info in certificate_infos:
            certificate_info.using = False
            db.session.add(certificate_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_certificate_info(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
        '''
        更新
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param data: dict 需要更新的数据
        :return: bool
        '''
        if data is None:
            data = {}
        if query_dict is None:
            query_dict = {}
        data = cls.reformatter_update(data)
        query = CertificateInfo.query.filter(CertificateInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, CertificateInfo)
            (certificate_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for certificate_info in certificate_infos:
            for key, value in data.items():
                if hasattr(certificate_info, key):
                    setattr(certificate_info, key, value)
            db.session.add(certificate_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]
        return v


class CertificateRank(db.Model):
    __tablename__ = 'certificate_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(80),default='' )
    using = Column(Boolean, default=True)

    @classmethod
    def reformatter_insert(cls, data: dict):
        return data

    @classmethod
    def reformatter_update(cls, data: dict):
        return data

    def dobule_to_dict(self):
        result = {}
        for key in self.__mapper__.c.keys():
            if getattr(self, key) is not None:
                result[key] = getattr(self, key)
            else:
                result[key] = getattr(self, key)
        return result

    # 配合多个对象使用的函数
    def to_json(all_vendors):
        v = [ven.dobule_to_dict() for ven in all_vendors]