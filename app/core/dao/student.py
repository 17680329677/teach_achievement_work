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




class Student(db.Model):
    __tablename__ = 'students'

    id = Column(INTEGER(11), primary_key=True)
    password = Column(String(255), default='' )
    name = Column(String(40), default='')
    gender = Column(String(20), default='')
    class_id = Column(INTEGER(11), default=0  )
    college_id = Column(INTEGER(11), default=0 )
    gpa = Column(Float(asdecimal=True), default=0)
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
    def formatter(cls, students):
        '''
        数据格式化
        :param students: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if students is None:
            return None
        try:
            students_dict = {
                'id': students.id,
                'password': students.password,
                'name': students.name,
                'gender': students.gender,
                'class_id': students.class_id,
                'college_id': students.college_id,
                'gpa': students.gpa
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return students_dict

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
        query = Student.query
        if not unscoped:
            query = query.filter(Student.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Student)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_students(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        students = Student()
        for key, value in data.items():
            if hasattr(Student, key):
                setattr(students, key, value)
        db.session.add(students)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_students(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        students = Student.query
        if not unscoped:
            students = students.filter(Student.using == True)
        try:
            students = students.filter(Student.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(students)

    @classmethod
    def query_students(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = Student.query
        if not unscoped:
            query = query.filter(Student.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Student)
            (studentss, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(students) for students in studentss], total

    @classmethod
    def delete_students(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = Student.query.filter(Student.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Student)
            (studentss, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for students in studentss:
            students.using = False
            db.session.add(students)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_students(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = Student.query.filter(Student.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Student)
            (studentss, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for students in studentss:
            for key, value in data.items():
                if hasattr(students, key):
                    setattr(students, key, value)
            db.session.add(students)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    def verify_password(self, password):
        return check_password_hash(self.password, password)  #如果密码正确return true

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



class ClassInfo(db.Model):
    __tablename__ = 'class_info'

    id = Column(INTEGER(11), primary_key=True)
    class_name = Column(String(255), default='' )
    college_id = Column(INTEGER(11), default=0  )
    grade = Column(String(60), default='' )
    status = Column(String(20), default='' )
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
    def formatter(cls, class_info):
        '''
        数据格式化
        :param class_info: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if class_info is None:
            return None
        try:
            class_info_dict = {
                'id': class_info.id,
                'class_name': class_info.class_name,
                'college_id': class_info.college_id,
                'grade': class_info.grade,
                'status': class_info.status,
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return class_info_dict

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
        query = ClassInfo.query
        if not unscoped:
            query = query.filter(ClassInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, ClassInfo)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_class_info(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        class_info = ClassInfo()
        for key, value in data.items():
            if hasattr(ClassInfo, key):
                setattr(class_info, key, value)
        db.session.add(class_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_class_info(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        class_info = ClassInfo.query
        if not unscoped:
            class_info = class_info.filter(ClassInfo.using == True)
        try:
            class_info = class_info.filter(ClassInfo.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(class_info)

    @classmethod
    def query_class_info(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = ClassInfo.query
        if not unscoped:
            query = query.filter(ClassInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, ClassInfo)
            (class_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(class_info) for class_info in class_infos], total

    @classmethod
    def delete_class_info(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = ClassInfo.query.filter(ClassInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, ClassInfo)
            (class_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for class_info in class_infos:
            class_info.using = False
            db.session.add(class_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_class_info(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = ClassInfo.query.filter(ClassInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, ClassInfo)
            (class_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for class_info in class_infos:
            for key, value in data.items():
                if hasattr(class_info, key):
                    setattr(class_info, key, value)
            db.session.add(class_info)
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




class DistributionInfo(db.Model):
    __tablename__ = 'distribution_info'

    id = Column(INTEGER(11), primary_key=True)
    college_id = Column(INTEGER(11), default=0  )
    orientation_name = Column(String(255), default='' )
    num_limit = Column(INTEGER(11), default=0 )
    start_time = Column(Date, default=datetime.now )
    end_time = Column(Date, default=datetime.now )
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
    def formatter(cls, distribution_info):
        '''
        数据格式化
        :param distribution_info: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if distribution_info is None:
            return None
        try:
            distribution_info_dict = {
                'id': distribution_info.id,
                'college_id': distribution_info.college_id,
                'orientation_name': distribution_info.orientation_name,
                'num_limit': distribution_info.num_limit,
                'start_time': distribution_info.start_time,
                'end_time': distribution_info.end_time
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return distribution_info_dict

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
        query = DistributionInfo.query
        if not unscoped:
            query = query.filter(DistributionInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionInfo)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_distribution_info(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        distribution_info = DistributionInfo()
        for key, value in data.items():
            if hasattr(DistributionInfo, key):
                setattr(distribution_info, key, value)
        db.session.add(distribution_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_distribution_info(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        distribution_info = DistributionInfo.query
        if not unscoped:
            distribution_info = distribution_info.filter(DistributionInfo.using == True)
        try:
            distribution_info = distribution_info.filter(DistributionInfo.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(distribution_info)

    @classmethod
    def query_distribution_info(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = DistributionInfo.query
        if not unscoped:
            query = query.filter(DistributionInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionInfo)
            (distribution_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(distribution_info) for distribution_info in distribution_infos], total

    @classmethod
    def delete_distribution_info(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = DistributionInfo.query.filter(DistributionInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionInfo)
            (distribution_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for distribution_info in distribution_infos:
            distribution_info.using = False
            db.session.add(distribution_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_distribution_info(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = DistributionInfo.query.filter(DistributionInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionInfo)
            (distribution_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for distribution_info in distribution_infos:
            for key, value in data.items():
                if hasattr(distribution_info, key):
                    setattr(distribution_info, key, value)
            db.session.add(distribution_info)
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




class DistributionDesire(db.Model):
    __tablename__ = 'distribution_desire'

    id = Column(INTEGER(11), primary_key=True)
    college_id = Column(INTEGER(11), default=0 )
    student_id = Column(INTEGER(11), default=0  )
    distribution_id = Column(INTEGER(11), default=0 )
    desire_rank = Column(INTEGER(11), default=0 )
    submit_time = Column(Date, default=datetime.now )
    status = Column(String(20), default='' )
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
    def formatter(cls, distribution_desire):
        '''
        数据格式化
        :param distribution_desire: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if distribution_desire is None:
            return None
        try:
            distribution_desire_dict = {
                'id': distribution_desire.id,
                'college_id': distribution_desire.college_id,
                'student_id': distribution_desire.student_id,
                'distribution_id': distribution_desire.distribution_id,
                'desire_rank': distribution_desire.desire_rank,
                'submit_time': distribution_desire.submit_time,
                'status': distribution_desire.status,
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return distribution_desire_dict

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
        query = DistributionDesire.query
        if not unscoped:
            query = query.filter(DistributionDesire.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionDesire)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_distribution_desire(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        distribution_desire = DistributionDesire()
        for key, value in data.items():
            if hasattr(DistributionDesire, key):
                setattr(distribution_desire, key, value)
        db.session.add(distribution_desire)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_distribution_desire(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        distribution_desire = DistributionDesire.query
        if not unscoped:
            distribution_desire = distribution_desire.filter(DistributionDesire.using == True)
        try:
            distribution_desire = distribution_desire.filter(DistributionDesire.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(distribution_desire)

    @classmethod
    def query_distribution_desire(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = DistributionDesire.query
        if not unscoped:
            query = query.filter(DistributionDesire.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionDesire)
            (distribution_desires, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(distribution_desire) for distribution_desire in distribution_desires], total

    @classmethod
    def delete_distribution_desire(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = DistributionDesire.query.filter(DistributionDesire.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionDesire)
            (distribution_desires, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for distribution_desire in distribution_desires:
            distribution_desire.using = False
            db.session.add(distribution_desire)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_distribution_desire(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = DistributionDesire.query.filter(DistributionDesire.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionDesire)
            (distribution_desires, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for distribution_desire in distribution_desires:
            for key, value in data.items():
                if hasattr(distribution_desire, key):
                    setattr(distribution_desire, key, value)
            db.session.add(distribution_desire)
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


class DistributionResult(db.Model):
    __tablename__ = 'distribution_result'

    id = Column(INTEGER(11), primary_key=True)
    college_id = Column(INTEGER(11), default=0 )
    student_id = Column(INTEGER(11), default=0  )
    distribution_id = Column(INTEGER(11), default=0 )
    status = Column(String(255), default='' )
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
    def formatter(cls, distribution_result):
        '''
        数据格式化
        :param distribution_result: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if distribution_result is None:
            return None
        try:
            distribution_result_dict = {
                'id': distribution_result.id,
                'college_id': distribution_result.college_id,
                'student_id': distribution_result.student_id,
                'distribution_id': distribution_result.distribution_id,
                'status': distribution_result.status
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return distribution_result_dict

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
        query = DistributionResult.query
        if not unscoped:
            query = query.filter(DistributionResult.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionResult)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_distribution_result(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        distribution_result = DistributionResult()
        for key, value in data.items():
            if hasattr(DistributionResult, key):
                setattr(distribution_result, key, value)
        db.session.add(distribution_result)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_distribution_result(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        distribution_result = DistributionResult.query
        if not unscoped:
            distribution_result = distribution_result.filter(DistributionResult.using == True)
        try:
            distribution_result = distribution_result.filter(DistributionResult.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(distribution_result)

    @classmethod
    def query_distribution_result(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = DistributionResult.query
        if not unscoped:
            query = query.filter(DistributionResult.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionResult)
            (distribution_results, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(distribution_result) for distribution_result in distribution_results], total

    @classmethod
    def delete_distribution_result(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = DistributionResult.query.filter(DistributionResult.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionResult)
            (distribution_results, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for distribution_result in distribution_results:
            distribution_result.using = False
            db.session.add(distribution_result)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_distribution_result(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = DistributionResult.query.filter(DistributionResult.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, DistributionResult)
            (distribution_results, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for distribution_result in distribution_results:
            for key, value in data.items():
                if hasattr(distribution_result, key):
                    setattr(distribution_result, key, value)
            db.session.add(distribution_result)
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


