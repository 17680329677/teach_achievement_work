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




class InnovationRank(db.Model):
    __tablename__ = 'innovation_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(80), default='' )
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
