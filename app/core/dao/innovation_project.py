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


class InnovationProject(db.Model):
    __tablename__ = 'innovation_project'

    id = Column(INTEGER(11), primary_key=True)
    project_name = Column(String(255), default='' )
    project_number = Column(String(80), default='' )
    rank_id = Column(INTEGER(11), default=0  )
    college_id = Column(INTEGER(11), default=0  )
    begin_year_month = Column(Date, default=datetime.now)
    mid_check_year_month = Column(Date, default=datetime.now)
    end_year_month = Column(Date, default=datetime.now)
    mid_check_rank = Column(String(50), default='')
    end_check_rank = Column(String(50), default='')
    subject = Column(String(60), default='')
    host_student = Column(String(255), default='' )
    participant_student = Column(String(255), default='')
    remark = Column(String(255), default='')
    submit_time = Column(Date, default=datetime.now)
    status = Column(String(60), default='' )
    using = Column(Boolean, default=True )

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
    def formatter(cls, innovation_project):
        '''
        数据格式化
        :param innovation_project: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if innovation_project is None:
            return None
        try:
            innovation_project_dict = {
                'id': innovation_project.id,
                'project_name': innovation_project.project_name,
                'project_number': innovation_project.project_number,
                'rank_id': innovation_project.rank_id,
                'college_id': innovation_project.college_id,
                'begin_year_month': innovation_project.begin_year_month,
                'mid_check_year_month': innovation_project.mid_check_year_month,
                'end_year_month': innovation_project.end_year_month,
                'mid_check_rank': innovation_project.mid_check_rank,
                'end_check_rank': innovation_project.end_check_rank,
                'subject': innovation_project.subject,
                'host_student': innovation_project.host_student,
                'participant_student': innovation_project.participant_student,
                'remark': innovation_project.remark,
                'submit_time': innovation_project.submit_time,
                'status': innovation_project.status
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return innovation_project_dict

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
        query = InnovationProject.query
        if not unscoped:
            query = query.filter(InnovationProject.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InnovationProject)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_innovation_project(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        innovation_project = InnovationProject()
        for key, value in data.items():
            if hasattr(InnovationProject, key):
                setattr(innovation_project, key, value)
        db.session.add(innovation_project)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_innovation_project(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        innovation_project = InnovationProject.query
        if not unscoped:
            innovation_project = innovation_project.filter(InnovationProject.using == True)
        try:
            innovation_project = innovation_project.filter(InnovationProject.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(innovation_project)

    @classmethod
    def query_innovation_project(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = InnovationProject.query
        if not unscoped:
            query = query.filter(InnovationProject.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InnovationProject)
            (innovation_projects, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(innovation_project) for innovation_project in innovation_projects], total

    @classmethod
    def delete_innovation_project(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = InnovationProject.query.filter(InnovationProject.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InnovationProject)
            (innovation_projects, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for innovation_project in innovation_projects:
            innovation_project.using = False
            db.session.add(innovation_project)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_innovation_project(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = InnovationProject.query.filter(InnovationProject.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InnovationProject)
            (innovation_projects, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for innovation_project in innovation_projects:
            for key, value in data.items():
                if hasattr(innovation_project, key):
                    setattr(innovation_project, key, value)
            db.session.add(innovation_project)
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




class InnovationRank(db.Model):
    __tablename__ = 'innovation_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(80), default='' )
    using = Column(Boolean, default=True)

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
    def formatter(cls, innovation_rank):
        '''
        数据格式化
        :param innovation_rank: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if innovation_rank is None:
            return None
        try:
            innovation_rank_dict = {
                'id': innovation_rank.id,
                'rank_name': innovation_rank.rank_name
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return innovation_rank_dict

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
        query = InnovationRank.query
        if not unscoped:
            query = query.filter(InnovationRank.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InnovationRank)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_innovation_rank(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        innovation_rank = InnovationRank()
        for key, value in data.items():
            if hasattr(InnovationRank, key):
                setattr(innovation_rank, key, value)
        db.session.add(innovation_rank)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_innovation_rank(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        innovation_rank = InnovationRank.query
        if not unscoped:
            innovation_rank = innovation_rank.filter(InnovationRank.using == True)
        try:
            innovation_rank = innovation_rank.filter(InnovationRank.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(innovation_rank)

    @classmethod
    def query_innovation_rank(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = InnovationRank.query
        if not unscoped:
            query = query.filter(InnovationRank.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InnovationRank)
            (innovation_ranks, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(innovation_rank) for innovation_rank in innovation_ranks], total

    @classmethod
    def delete_innovation_rank(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = InnovationRank.query.filter(InnovationRank.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InnovationRank)
            (innovation_ranks, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for innovation_rank in innovation_ranks:
            innovation_rank.using = False
            db.session.add(innovation_rank)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_innovation_rank(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = InnovationRank.query.filter(InnovationRank.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InnovationRank)
            (innovation_ranks, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for innovation_rank in innovation_ranks:
            for key, value in data.items():
                if hasattr(innovation_rank, key):
                    setattr(innovation_rank, key, value)
            db.session.add(innovation_rank)
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
