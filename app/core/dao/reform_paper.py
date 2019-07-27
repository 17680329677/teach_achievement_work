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


class TeachReformPaper(db.Model):
    __tablename__ = 'teach_reform_paper'

    id = Column(INTEGER(11), primary_key=True)
    paper_name = Column(String(255), default='')
    paper_number = Column(INTEGER(11), default=0)
    journal_name = Column(String(255), default='')
    publish_year_month = Column(Date, default=datetime.now)
    journal_year = Column(String(255), default='')
    journal_number = Column(String(255), default='')
    journal_volum = Column(String(255), default='')
    source_project = Column(String(255), default='')
    cover_path = Column(String(255), default='')
    content_path = Column(String(255), default='')
    text_path = Column(String(255), default='')
    cnki_url = Column(String(255), default='')
    participate_teacher = Column(String(255), default='')
    college_id = Column(INTEGER(11), default=0)
    status = Column(String(40), default='')
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
    def formatter(cls, teach_reform_paper):
        '''
        数据格式化
        :param teach_reform_paper: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if teach_reform_paper is None:
            return None
        try:
            teach_reform_paper_dict = {
                'id': teach_reform_paper.id,
                'paper_name': teach_reform_paper.paper_name,
                'paper_number': teach_reform_paper.paper_number,
                'journal_name': teach_reform_paper.journal_name,
                'publish_year_month': teach_reform_paper.publish_year_month,
                'journal_year': teach_reform_paper.journal_year,
                'journal_number': teach_reform_paper.journal_number,
                'journal_volum': teach_reform_paper.journal_volum,
                'source_project': teach_reform_paper.source_project,
                'cover_path': teach_reform_paper.cover_path,
                'content_path': teach_reform_paper.content_path,
                'text_path': teach_reform_paper.text_path,
                'cnki_url': teach_reform_paper.cnki_url,
                'participate_teacher': teach_reform_paper.participate_teacher,
                'college_id': teach_reform_paper.college_id,
                'status': teach_reform_paper.status
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return teach_reform_paper_dict

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
        query = TeachReformPaper.query
        if not unscoped:
            query = query.filter(TeachReformPaper.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeachReformPaper)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_teach_reform_paper(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        teach_reform_paper = TeachReformPaper()
        for key, value in data.items():
            if hasattr(TeachReformPaper, key):
                setattr(teach_reform_paper, key, value)
        db.session.add(teach_reform_paper)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_teach_reform_paper(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        teach_reform_paper = TeachReformPaper.query
        if not unscoped:
            teach_reform_paper = teach_reform_paper.filter(TeachReformPaper.using == True)
        try:
            teach_reform_paper = teach_reform_paper.filter(TeachReformPaper.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(teach_reform_paper)

    @classmethod
    def query_teach_reform_paper(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = TeachReformPaper.query
        if not unscoped:
            query = query.filter(TeachReformPaper.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeachReformPaper)
            (teach_reform_papers, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(teach_reform_paper) for teach_reform_paper in teach_reform_papers], total

    @classmethod
    def delete_teach_reform_paper(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = TeachReformPaper.query.filter(TeachReformPaper.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeachReformPaper)
            (teach_reform_papers, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teach_reform_paper in teach_reform_papers:
            teach_reform_paper.using = False
            db.session.add(teach_reform_paper)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_teach_reform_paper(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = TeachReformPaper.query.filter(TeachReformPaper.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeachReformPaper)
            (teach_reform_papers, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teach_reform_paper in teach_reform_papers:
            for key, value in data.items():
                if hasattr(teach_reform_paper, key):
                    setattr(teach_reform_paper, key, value)
            db.session.add(teach_reform_paper)
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





