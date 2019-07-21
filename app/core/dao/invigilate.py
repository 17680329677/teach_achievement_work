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




class SemesterInfo(db.Model):
    __tablename__ = 'semester_info'

    id = Column(INTEGER(11), primary_key=True)
    semester_name = Column(String(80), default='')
    status = Column(String(20), default='')
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
        return data

    @classmethod
    def reformatter_update(cls, data: dict):
        return data

