from app import db
from werkzeug.security import check_password_hash

from sqlalchemy import Column, DateTime, Float , String, Boolean, Date
from sqlalchemy.dialects.mysql import INTEGER,BIGINT

from app.utils.url_condition.url_condition_mysql import UrlCondition, process_query, count_query, page_query
from app.utils.Error import CustomError
from datetime import datetime

from flask_login import UserMixin

class Teacher(UserMixin, db.Model):
    __tablename__ = 'teacher'

    id = Column(INTEGER(11), primary_key=True)
    number = Column(String(60), default='')
    password = Column(String(255), default='')
    type = Column(INTEGER(11), default=5) #5是教师系列
    using = Column(Boolean, default=True)

    def __repr__(self):
        return '<Teacher %r>' % self.number

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
    def formatter(cls, teacher):
        '''
        数据格式化
        :param teacher: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if teacher is None:
            return None
        try:
            teacher_dict = {
                'id': teacher.id,
                'number': teacher.number,
                'password': teacher.password,
                'type': teacher.type
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return teacher_dict

    @classmethod
    def count(cls,query_dict: dict, unscoped: bool = False):
        '''
        计数
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: total int 查询数量的结果
        '''
        if query_dict is None:
            query_dict = {}
        query = Teacher.query
        if not unscoped:
            query = query.filter(Teacher.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query,url_condition.filter_dict, url_condition.sort_limit_dict, Teacher)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_teacher(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        teacher = Teacher()
        for key, value in data.items():
            if hasattr(Teacher, key):
                setattr(teacher, key, value)
        db.session.add(teacher)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_teacher(cls, number: String, unscoped: bool = False):
        '''
        查：获取一行
        :param number: String 教师账号
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        teacher = Teacher.query
        if not unscoped:
            teacher = teacher.filter(Teacher.using == True)
        try:
            teacher = teacher.filter(Teacher.number == number).first()
        except Exception as e:
            raise  CustomError(500, 500, str(e))
        return cls.formatter(teacher)

    @classmethod
    def query_teacher(cls, query_dict = None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = Teacher.query
        if not unscoped:
            query = query.filter(Teacher.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Teacher)
            (teachers, total) = page_query(query,url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(teacher) for teacher in teachers], total

    @classmethod
    def delete_teacher(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = Teacher.query.filter(Teacher.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Teacher)
            (teachers, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher in teachers:
            teacher.using = False
            db.session.add(teacher)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_teacher(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = Teacher.query.filter(Teacher.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Teacher)
            (teachers, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher in teachers:
            for key, value in data.items():
                if hasattr(teacher, key):
                    setattr(teacher, key, value)
            db.session.add(teacher)
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


class TeacherType(db.Model):
    __tablename__ = 'teacher_type'

    id = Column(INTEGER(11), primary_key=True)
    type_name = Column(String(255), default='')
    role = Column(String(255), default='')
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
    def formatter(cls, teacher_type):
        '''
        数据格式化
        :param teacher: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if teacher_type is None:
            return None
        try:
            teacher_type_dict = {
                'id': teacher_type.id,
                'type_name': teacher_type.type_name,
                'role': teacher_type.role,
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return teacher_type_dict

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
        query = TeacherType.query
        if not unscoped:
            query = query.filter(TeacherType.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherType)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_teacher_type(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        teacher_type = TeacherType()
        for key, value in data.items():
            if hasattr(TeacherType, key):
                setattr(TeacherType, key, value)
        db.session.add(teacher_type)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_teacher_type(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param number: String 教师账号
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        teacher_type = TeacherType.query
        if not unscoped:
            teacher_type = teacher_type.filter(TeacherType.using == True)
        try:
            teacher_type = teacher_type.filter(TeacherType.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(teacher_type)

    @classmethod
    def query_teacher_type(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = TeacherType.query
        if not unscoped:
            query = query.filter(TeacherType.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherType)
            (teacher_types, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(teacher_type) for teacher_type in teacher_types], total

    @classmethod
    def delete_teacher_type(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = TeacherType.query.filter(TeacherType.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherType)
            (teacher_types, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher_type in teacher_types:
            teacher_type.using = False
            db.session.add(teacher_type)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_teacher_type(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = TeacherType.query.filter(TeacherType.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherType)
            (teacher_types, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher_type in teacher_types:
            for key, value in data.items():
                if hasattr(teacher_type, key):
                    setattr(teacher_type, key, value)
            db.session.add(teacher_type)
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

class TeacherInfo(db.Model):
    __tablename__ = 'teacher_info'

    id = Column(INTEGER(11), primary_key=True)
    number = Column(String(60),default='')
    name = Column(String(100),default='')
    gender = Column(String(20),default='')
    nationality = Column(String(20),default='')
    birth_year_month = Column(Date, default=datetime.now )
    college_id = Column(INTEGER(11), default=0)
    department_id = Column(INTEGER(11), default=0)
    teachertitle_id = Column(INTEGER(11), default=0 )
    managertitle_id = Column(INTEGER(11), default=0 )
    teacher_category_id = Column(INTEGER(11), default=0 )
    type = Column(String(20), default=0)
    type_id = Column(INTEGER(11), default=0)
    work_begin_year_month = Column(Date, default=datetime.now)
    bjfu_join_year_month = Column(Date, default=datetime.now)
    highest_education = Column(String(255), default='')
    highest_education_accord_year_month = Column(Date, default=datetime.now)
    graduate_paper_title = Column(String(255), default='')
    graduate_school = Column(String(255), default='')
    research_direction = Column(String(255), default='')
    telephone = Column(String(60), default='')
    email = Column(String(255), default='')
    status = Column(String(60), default='')
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
    def formatter(cls, teacher_info):
        '''
        数据格式化
        :param teacher_info: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if teacher_info is None:
            return None
        try:
            teacher_info_dict = {
                'id': teacher_info.id,
                'number': teacher_info.number,
                'name': teacher_info.name,
                'gender': teacher_info.gender,
                'nationality': teacher_info.nationality,
                'birth_year_month': teacher_info.birth_year_month,
                'college_id': teacher_info.college_id,
                'department_id': teacher_info.department_id,
                'teachertitle_id': teacher_info.teachertitle_id,
                'managertitle_id': teacher_info.managertitle_id,
                'teacher_category_id': teacher_info.teacher_category_id,
                'type': teacher_info.type,
                'type_id': teacher_info.type_id,
                'work_begin_year_month': teacher_info.work_begin_year_month,
                'bjfu_join_year_month': teacher_info.bjfu_join_year_month,
                'highest_education': teacher_info.highest_education,
                'highest_education_accord_year_month': teacher_info.highest_education_accord_year_month,
                'graduate_paper_title': teacher_info.graduate_paper_title,
                'graduate_school': teacher_info.graduate_school,
                'research_direction': teacher_info.research_direction,
                'telephone': teacher_info.telephone,
                'email': teacher_info.email,
                'status': teacher_info.status,
                'using': teacher_info.using,
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return teacher_info_dict

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
        query = TeacherInfo.query
        if not unscoped:
            query = query.filter(TeacherInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherInfo)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_teacher_info(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        teacher_info = TeacherInfo()
        for key, value in data.items():
            if hasattr(TeacherInfo, key):
                setattr(TeacherInfo, key, value)
        db.session.add(teacher_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_teacher_info(cls, number: String, unscoped: bool = False):
        '''
        查：获取一行
        :param number: String 教师账号
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        teacher_info = TeacherInfo.query
        if not unscoped:
            teacher_info = teacher_info.filter(TeacherInfo.using == True)
        try:
            teacher_info = teacher_info.filter(TeacherInfo.number == number).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(teacher_info)

    @classmethod
    def query_teacher_info(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = TeacherInfo.query
        if not unscoped:
            query = query.filter(TeacherInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherInfo)
            (teacher_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(teacher_info) for teacher_info in teacher_infos], total

    @classmethod
    def delete_teacher_info(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = TeacherInfo.query.filter(TeacherInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherInfo)
            (teacher_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher_info in teacher_infos:
            teacher_info.using = False
            db.session.add(teacher_info)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_teacher_info(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = TeacherInfo.query.filter(TeacherInfo.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherInfo)
            (teacher_infos, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher_info in teacher_infos:
            for key, value in data.items():
                if hasattr(teacher_info, key):
                    setattr(teacher_info, key, value)
            db.session.add(teacher_info)
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



class TeacherTitle(db.Model):
    __tablename__ = 'teacher_title'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), default='' )
    teacher_category_id = Column(INTEGER(11), default=0)
    using = Column(Boolean, default=True)

    def __repr__(self):
        return '<TeacherTitle %r>' % self.name

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
    def formatter(cls, teacher_title):
        '''
        数据格式化
        :param teacher_title: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if teacher_title is None:
            return None
        try:
            teacher_title_dict = {
                'id': teacher_title.id,
                'name': teacher_title.name,
                'teacher_category_id': teacher_title.teacher_category_id,
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return teacher_title_dict

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
        query = TeacherTitle.query
        if not unscoped:
            query = query.filter(TeacherTitle.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherTitle)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_teacher_title(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        teacher_title = TeacherTitle()
        for key, value in data.items():
            if hasattr(TeacherTitle, key):
                setattr(teacher_title, key, value)
        db.session.add(teacher_title)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_teacher_title(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int    id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        teacher_title = TeacherTitle.query
        if not unscoped:
            teacher_title = teacher_title.filter(TeacherTitle.using == True)
        try:
            teacher_title = teacher_title.filter(TeacherTitle.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(teacher_title)

    @classmethod
    def query_teacher_title(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = TeacherTitle.query
        if not unscoped:
            query = query.filter(TeacherTitle.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherTitle)
            (teacher_titles, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(teacher_title) for teacher_title in teacher_titles], total

    @classmethod
    def delete_teacher_title(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = TeacherTitle.query.filter(TeacherTitle.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherTitle)
            (teacher_titles, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher_title in teacher_titles:
            teacher_title.using = False
            db.session.add(teacher_title)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_teacher_title(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = TeacherTitle.query.filter(TeacherTitle.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherTitle)
            (teacher_titles, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher_title in teacher_titles:
            for key, value in data.items():
                if hasattr(teacher_title, key):
                    setattr(teacher_title, key, value)
            db.session.add(teacher_title)
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




class TeacherCategory(db.Model):
    __tablename__ = 'teacher_category'

    id = Column(INTEGER(11), primary_key=True)
    name = Column(String(255), default='')
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
    def formatter(cls, teacher_category):
        '''
        数据格式化
        :param teacher_category: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if teacher_category is None:
            return None
        try:
            teacher_category_dict = {
                'id': teacher_category.id,
                'name': teacher_category.name,
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return teacher_category_dict

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
        query = TeacherCategory.query
        if not unscoped:
            query = query.filter(TeacherCategory.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherCategory)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_teacher_category(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        teacher_category = TeacherCategory()
        for key, value in data.items():
            if hasattr(TeacherCategory, key):
                setattr(teacher_category, key, value)
        db.session.add(teacher_category)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_teacher_category(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        teacher_category = TeacherCategory.query
        if not unscoped:
            teacher_category = teacher_category.filter(TeacherCategory.using == True)
        try:
            teacher_category = teacher_category.filter(TeacherCategory.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(teacher_category)

    @classmethod
    def query_teacher_category(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = TeacherCategory.query
        if not unscoped:
            query = query.filter(TeacherCategory.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherCategory)
            (teacher_categorys, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(teacher_category) for teacher_category in teacher_categorys], total

    @classmethod
    def delete_teacher_category(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = TeacherCategory.query.filter(TeacherCategory.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherCategory)
            (teacher_categorys, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher_category in teacher_categorys:
            teacher_category.using = False
            db.session.add(teacher_category)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_teacher_category(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = TeacherCategory.query.filter(TeacherCategory.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TeacherCategory)
            (teacher_categorys, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for teacher_category in teacher_categorys:
            for key, value in data.items():
                if hasattr(teacher_category, key):
                    setattr(teacher_category, key, value)
            db.session.add(teacher_category)
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



class TitleRecord(db.Model):
    __tablename__ = 'title_record'

    id = Column(INTEGER(11), primary_key=True)
    datetime = Column(Date, default=datetime.now )
    teacher_number = Column(String(60), default=''  )
    teacher_title_id = Column(INTEGER(11), default=0 )
    manager_title_id = Column(INTEGER(11), default=0 )
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
    def formatter(cls, title_record):
        '''
        数据格式化
        :param title_record: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if title_record is None:
            return None
        try:
            title_record_dict = {
                'id': title_record.id,
                'datetime': title_record.datetime,
                'teacher_number': title_record.teacher_number,
                'teacher_title_id': title_record.teacher_title_id,
                'manager_title_id': title_record.manager_title_id
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return title_record_dict

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
        query = TitleRecord.query
        if not unscoped:
            query = query.filter(TitleRecord.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TitleRecord)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_title_record(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        title_record = TitleRecord()
        for key, value in data.items():
            if hasattr(TitleRecord, key):
                setattr(title_record, key, value)
        db.session.add(title_record)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_title_record(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        title_record = TitleRecord.query
        if not unscoped:
            title_record = title_record.filter(TitleRecord.using == True)
        try:
            title_record = title_record.filter(TitleRecord.int == int).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(title_record)

    @classmethod
    def query_title_record(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = TitleRecord.query
        if not unscoped:
            query = query.filter(TitleRecord.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TitleRecord)
            (title_records, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(title_record) for title_record in title_records], total

    @classmethod
    def delete_title_record(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = TitleRecord.query.filter(TitleRecord.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TitleRecord)
            (title_records, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for title_record in title_records:
            title_record.using = False
            db.session.add(title_record)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_title_record(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = TitleRecord.query.filter(TitleRecord.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, TitleRecord)
            (title_records, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for title_record in title_records:
            for key, value in data.items():
                if hasattr(title_record, key):
                    setattr(title_record, key, value)
            db.session.add(title_record)
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