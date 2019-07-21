from app import db
from werkzeug.security import check_password_hash

from sqlalchemy import Column, DateTime, Float, ForeignKey, String, Boolean, Date
from sqlalchemy.dialects.mysql import INTEGER,BIGINT
from sqlalchemy.orm import relationship

from app.utils.url_condition.url_condition_mysql import UrlCondition, process_query, count_query, page_query
from app.utils.Error import CustomError
from datetime import datetime

class Book(db.Model):
    __tablename__ = 'book'

    id = Column(INTEGER(11), primary_key=True)
    book_name = Column(String(255), default='')
    publish_year_month = Column(Date, default=datetime.now)
    pages = Column(INTEGER(11), default=0)
    words = Column(INTEGER(11), default=0)
    isbn = Column(String(255), default='')
    press = Column(String(100), default='')
    version = Column(String(60), default='')
    style = Column(String(60), default='')
    rank_id = Column(INTEGER(11), default=0 )
    college_id = Column(INTEGER(11), default=0  )
    source_project = Column(String(255), default='')
    cover_path = Column(String(255), default='')
    copyright_path = Column(String(255), default='')
    content_path = Column(String(255), default='')
    participate_teacher = Column(String(255), default='')
    submit_teacher = Column(String(255), default='')
    submit_time = Column(Date, default=datetime.now)
    status = Column(String(255), default='')
    using = Column(Boolean, default=True )

    @classmethod
    def reformatter_insert(cls, data: dict):
        return data

    @classmethod
    def reformatter_update(cls, data: dict):
        return data

    def __repr__(self):
        return '<Book %r>' % self.book_name

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





class BookRank(db.Model):
    __tablename__ = 'book_rank'

    id = Column(INTEGER(11), primary_key=True)
    rank_name = Column(String(255), default='')
    using = Column(Boolean, default=True)

    @classmethod
    def reformatter_insert(cls, data: dict):
        return data

    @classmethod
    def reformatter_update(cls, data: dict):
        return data

    def __repr__(self):
        return '<BookRank %r>' % self.rank_name

    def single_to_dict(self):
        return {c.name: getattr(self, c.name) for c in self.__table__.columns}

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