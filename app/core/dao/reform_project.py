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

class TeachReformProject(db.Model):
    __tablename__ = 'teach_reform_project'

    id = Column(INTEGER(11), primary_key=True)
    project_name = Column(String(255), default='' )
    project_number = Column(String(255), default='')
    type_child_id = Column(INTEGER(11), default=0  )
    rank_id = Column(INTEGER(11), default=0  )
    college_id = Column(INTEGER(11), default=0  )
    begin_year_month = Column(Date, default=datetime.now)
    mid_check_year_month = Column(Date, default=datetime.now)
    mid_check_rank = Column(String(20), default='')
    end_year_month = Column(Date, default=datetime.now)
    end_check_rank = Column(String(20), default='')
    subject = Column(String(80), default='')
    host_person = Column(String(255), default='')
    participate_person = Column(String(255), default='')
    remark = Column(String(255), default='')
    grade = Column(String(255), default='')
    submit_time = Column(Date, default=datetime.now )
    status = Column(String(20), default='')
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
    def formatter(cls, teach_reform_project):
        '''
        数据格式化
        :param teach_reform_project: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if teach_reform_project is None:
            return None
        try:
            teach_reform_project_dict = {
                'id': teach_reform_project.id,
                'project_name': teach_reform_project.project_name,
                'project_number': teach_reform_project.project_number,
                'type_child_id': teach_reform_project.type_child_id,
                'rank_id': teach_reform_project.rank_id,
                'college_id': teach_reform_project.college_id,
                'begin_year_month': teach_reform_project.begin_year_month,
                'mid_check_year_month': teach_reform_project.mid_check_year_month,
                'mid_check_rank': teach_reform_project.mid_check_rank,
                'end_year_month': teach_reform_project.end_year_month,
                'end_check_rank': teach_reform_project.end_check_rank,
                'subject': teach_reform_project.subject,
                'host_person': teach_reform_project.host_person,
                'participate_person': teach_reform_project.participate_person,
                'remark': teach_reform_project.remark,
                'grade': teach_reform_project.grade,
                'submit_time': teach_reform_project.submit_time,
                'status': teach_reform_project.status
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return teach_reform_project_dict

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
        query = TeachReformProject.query
        if not unscoped:
            query = query.filter(TeachReformProject.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeachReformProject)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_teach_reform_project(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        teach_reform_project = TeachReformProject()
        for key, value in data.items():
            if hasattr(TeachReformProject, key):
                setattr(teach_reform_project, key, value)
        db.session.add(teach_reform_project)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_teach_reform_project(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        teach_reform_project = TeachReformProject.query
        if not unscoped:
            teach_reform_project = teach_reform_project.filter(TeachReformProject.using == True)
        try:
            teach_reform_project = teach_reform_project.filter(TeachReformProject.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(teach_reform_project)

    @classmethod
    def query_teach_reform_project(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = TeachReformProject.query
        if not unscoped:
            query = query.filter(TeachReformProject.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeachReformProject)
            (teach_reform_projects, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(teach_reform_project) for teach_reform_project in teach_reform_projects], total

    @classmethod
    def delete_teach_reform_project(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = TeachReformProject.query.filter(TeachReformProject.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeachReformProject)
            (teach_reform_projects, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teach_reform_project in teach_reform_projects:
            teach_reform_project.using = False
            db.session.add(teach_reform_project)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_teach_reform_project(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = TeachReformProject.query.filter(TeachReformProject.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeachReformProject)
            (teach_reform_projects, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teach_reform_project in teach_reform_projects:
            for key, value in data.items():
                if hasattr(teach_reform_project, key):
                    setattr(teach_reform_project, key, value)
            db.session.add(teach_reform_project)
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


class ProjectType(db.Model):
    __tablename__ = 'project_type'

    id = Column(INTEGER(11), primary_key=True)
    type_name = Column(String(255), default='' )
    student_attend = Column(String(20), default='' )
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
        return v



class ProjectChildType(db.Model):
    __tablename__ = 'project_child_type'

    id = Column(INTEGER(11), primary_key=True)
    child_type_name = Column(String(255), default='' )
    parent_type_id = Column(INTEGER(11), default=0  )
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
        return v



class ProjectRank(db.Model):
    __tablename__ = 'project_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(255), default='' )
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
        return v



class ProjectChangeRecord(db.Model):
    __tablename__ = 'project_change_record'

    id = Column(INTEGER(11), primary_key=True)
    project_id = Column(INTEGER(11), default=0  )
    reason = Column(String(255), default='' )
    change_time = Column(Date, default=datetime.now)
    describe = Column(String(255), default='' )
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
        return v

