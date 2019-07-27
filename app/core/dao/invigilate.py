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



class InvigilateInfo(db.Model):
    __tablename__ = 'invigilate_info'

    id = Column(INTEGER(11), primary_key=True)
    apply_teacher = Column(String(255), default=''  )
    subject = Column(INTEGER(11), default=0  )
    semester_id = Column(INTEGER(11), default=0 )
    _class = Column('class', String(255), default='' )
    exam_time = Column(Date, default=datetime.now)
    location = Column(String(255), default='' )
    participate_teacher = Column(String(255), default='' )
    submit_time = Column(Date, default=datetime.now)
    college_id = Column(INTEGER(11), default=0 )
    status = Column(String(80), default='')
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
    def formatter(cls, invigilate_info):
        '''
        数据格式化
        :param invigilate_info: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if invigilate_info is None:
            return None
        try:
            invigilate_info_dict = {
                'id': invigilate_info.id,
                'apply_teacher': invigilate_info.apply_teacher,
                'subject': invigilate_info.subject,
                'semester_id': invigilate_info.semester_id,
                '_class': invigilate_info._class,
                'exam_time': invigilate_info.exam_time,
                'location': invigilate_info.location,
                'participate_teacher': invigilate_info.participate_teacher,
                'submit_time': invigilate_info.submit_time,
                'college_id': invigilate_info.college_id,
                'status': invigilate_info.status
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return invigilate_info_dict

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
        query = InvigilateInfo.query
        if not unscoped:
            query = query.filter(InvigilateInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InvigilateInfo)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_invigilate_info(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        invigilate_info = InvigilateInfo()
        for key, value in data.items():
            if hasattr(InvigilateInfo, key):
                setattr(invigilate_info, key, value)
        db.session.add(invigilate_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_invigilate_info(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        invigilate_info = InvigilateInfo.query
        if not unscoped:
            invigilate_info = invigilate_info.filter(InvigilateInfo.using == True)
        try:
            invigilate_info = invigilate_info.filter(InvigilateInfo.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(invigilate_info)

    @classmethod
    def query_invigilate_info(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = InvigilateInfo.query
        if not unscoped:
            query = query.filter(InvigilateInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InvigilateInfo)
            (invigilate_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(invigilate_info) for invigilate_info in invigilate_infos], total

    @classmethod
    def delete_invigilate_info(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = InvigilateInfo.query.filter(InvigilateInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InvigilateInfo)
            (invigilate_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for invigilate_info in invigilate_infos:
            invigilate_info.using = False
            db.session.add(invigilate_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_invigilate_info(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = InvigilateInfo.query.filter(InvigilateInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, InvigilateInfo)
            (invigilate_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for invigilate_info in invigilate_infos:
            for key, value in data.items():
                if hasattr(invigilate_info, key):
                    setattr(invigilate_info, key, value)
            db.session.add(invigilate_info)
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




class SemesterInfo(db.Model):
    __tablename__ = 'semester_info'

    id = Column(INTEGER(11), primary_key=True)
    semester_name = Column(String(80), default='')
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
    def formatter(cls, semester_info):
        '''
        数据格式化
        :param semester_info: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if semester_info is None:
            return None
        try:
            semester_info_dict = {
                'id': semester_info.id,
                'semester_name': semester_info.semester_name,
                'status': semester_info.status
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return semester_info_dict

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
        query = Course.query
        if not unscoped:
            query = query.filter(Course.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Course)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_semester_info(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        semester_info = Course()
        for key, value in data.items():
            if hasattr(Course, key):
                setattr(semester_info, key, value)
        db.session.add(semester_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_semester_info(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        semester_info = Course.query
        if not unscoped:
            semester_info = semester_info.filter(Course.using == True)
        try:
            semester_info = semester_info.filter(Course.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(semester_info)

    @classmethod
    def query_semester_info(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = Course.query
        if not unscoped:
            query = query.filter(Course.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Course)
            (semester_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(semester_info) for semester_info in semester_infos], total

    @classmethod
    def delete_semester_info(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = Course.query.filter(Course.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Course)
            (semester_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for semester_info in semester_infos:
            semester_info.using = False
            db.session.add(semester_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_semester_info(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = Course.query.filter(Course.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Course)
            (semester_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for semester_info in semester_infos:
            for key, value in data.items():
                if hasattr(semester_info, key):
                    setattr(semester_info, key, value)
            db.session.add(semester_info)
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



class Course(db.Model):
    __tablename__ = 'course'

    id = Column(INTEGER(11), primary_key=True)
    course_name = Column(String(255), default='')
    category = Column(String(20), default='')
    all_teaching_time = Column(INTEGER(11), default=0)
    credit = Column(Float(asdecimal=True), default=0)
    classes = Column(String(255), default='')
    choose_number = Column(INTEGER(11), default=0)
    teacher = Column(String(255), default='')
    submit_time = Column(Date, default=datetime.now)
    college_id = Column(INTEGER(11), default=0)
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
    def formatter(cls, course):
        '''
        数据格式化
        :param course: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if course is None:
            return None
        try:
            course_dict = {
                'id': course.id,
                'course_name': course.course_name,
                'category': course.category,
                'all_teaching_time': course.all_teaching_time,
                'credit': course.credit,
                'classes': course.classes,
                'choose_number': course.choose_number,
                'teacher': course.teacher,
                'submit_time': course.submit_time,
                'college_id': course.college_id,
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return course_dict

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
        query = Course.query
        if not unscoped:
            query = query.filter(Course.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Course)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_course(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        course = Course()
        for key, value in data.items():
            if hasattr(Course, key):
                setattr(course, key, value)
        db.session.add(course)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_course(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        course = Course.query
        if not unscoped:
            course = course.filter(Course.using == True)
        try:
            course = course.filter(Course.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(course)

    @classmethod
    def query_course(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = Course.query
        if not unscoped:
            query = query.filter(Course.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Course)
            (courses, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(course) for course in courses], total

    @classmethod
    def delete_course(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = Course.query.filter(Course.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Course)
            (courses, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for course in courses:
            course.using = False
            db.session.add(course)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_course(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = Course.query.filter(Course.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Course)
            (courses, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for course in courses:
            for key, value in data.items():
                if hasattr(course, key):
                    setattr(course, key, value)
            db.session.add(course)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

