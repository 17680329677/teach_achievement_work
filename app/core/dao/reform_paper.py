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





