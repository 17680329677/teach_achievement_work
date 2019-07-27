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
    def formatter(cls, book):
        '''
        数据格式化
        :param book: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if book is None:
            return None
        try:
            book_dict = {
                'id' : book.id,
                'book_name' : book.book_name,
                'publish_year_month' : book.publish_year_month,
                'pages' : book.pages,
                'words' : book.words,
                'isbn' : book.isbn,
                'press' : book.press,
                'version' : book.version,
                'style' : book.style,
                'rank_id' : book.rank_id,
                'college_id' : book.college_id,
                'source_project' : book.source_project,
                'cover_path' : book.cover_path,
                'copyright_path' : book.copyright_path,
                'content_path' : book.content_path,
                'participate_teacher' : book.participate_book_rank,
                'submit_teacher' : book.submit_book_rank,
                'submit_time' : book.submit_time,
                'status' : book.status,
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return book_dict

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
        query = Book.query
        if not unscoped:
            query = query.filter(Book.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Book)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_book(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        book = Book()
        for key, value in data.items():
            if hasattr(Book, key):
                setattr(book, key, value)
        db.session.add(book)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_book(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        book = Book.query
        if not unscoped:
            book = book.filter(Book.using == True)
        try:
            book = book.filter(Book.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(book)

    @classmethod
    def query_book(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = Book.query
        if not unscoped:
            query = query.filter(Book.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Book)
            (books, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(book) for book in books], total

    @classmethod
    def delete_book(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = Book.query.filter(Book.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Book)
            (books, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for book in books:
            book.using = False
            db.session.add(book)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_book(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = Book.query.filter(Book.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, Book)
            (books, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for book in books:
            for key, value in data.items():
                if hasattr(book, key):
                    setattr(book, key, value)
            db.session.add(book)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

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
    def formatter(cls, book_rank):
        '''
        数据格式化
        :param book_rank: 实例化的DAO db对象
        :return: dict 转化后的表数据，负责将数据库中存储的数据转化成你想要的，比如id索引到名称的转换
        '''
        if book_rank is None:
            return None
        try:
            book_rank_dict = {
                'id': book_rank.id,
                'rank_name': book_rank.rank_name
            }
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return book_rank_dict

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
        query = BookRank.query
        if not unscoped:
            query = query.filter(BookRank.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            total = count_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, BookRank)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return total

    @classmethod
    def insert_book_rank(cls, ctx: bool = True, data: dict = None):
        '''
        增加
        :param ctx: bool ctx means context 表示上下文，但是没有封装context进去，现只表示：是否使用事务。因为DAO层会有相互调用，需要事务处理。
        :param data:
        :return: bool True
        '''
        if data is None:
            data = {}
        data = cls.reformatter_insert(data)
        book_rank = BookRank()
        for key, value in data.items():
            if hasattr(BookRank, key):
                setattr(book_rank, key, value)
        db.session.add(book_rank)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def get_book_rank(cls, id: int, unscoped: bool = False):
        '''
        查：获取一行
        :param id: int id
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return:
        '''
        book_rank = BookRank.query
        if not unscoped:
            book_rank = book_rank.filter(BookRank.using == True)
        try:
            book_rank = book_rank.filter(BookRank.id == id).first()
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return cls.formatter(book_rank)

    @classmethod
    def query_book_rank(cls, query_dict=None, unscoped: bool = False):
        '''
        查：获取多行数据
        :param query_dict: dict 带有查询命令和数据的dict字典
        :param unscoped: bool 是否查询软删除，默认是不查询
        :return: list, int  多行list数据， 多少条数据
        '''
        if query_dict is None:
            query_dict = {}
        query = BookRank.query
        if not unscoped:
            query = query.filter(BookRank.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, BookRank)
            (book_ranks, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        return [cls.formatter(book_rank) for book_rank in book_ranks], total

    @classmethod
    def delete_book_rank(cls, ctx: bool = True, query_dict: dict = None):
        '''
        软删除
        :param ctx: bool 是否使用事务。
        :param query_dict: dict 带有查询命令和数据的dict字典
        :return: bool True
        '''
        if query_dict is None:
            query_dict = {}
        query = BookRank.query.filter(BookRank.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, BookRank)
            (book_ranks, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for book_rank in book_ranks:
            book_rank.using = False
            db.session.add(book_rank)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def update_book_rank(cls, ctx: bool = True, query_dict: dict = None, data: dict = None):
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
        query = BookRank.query.filter(BookRank.using == True)
        url_condition = UrlCondition(query_dict)
        try:
            query = process_query(query, url_condition.filter_dict, url_condition.sort_limit_dict, BookRank)
            (book_ranks, total) = page_query(query, url_condition.page_dict)
        except Exception as e:
            raise CustomError(500, 500, str(e))
        for book_rank in book_ranks:
            for key, value in data.items():
                if hasattr(book_rank, key):
                    setattr(book_rank, key, value)
            db.session.add(book_rank)
        if ctx:
            try:
                db.session.commit()
            except Exception as e:
                raise CustomError(500, 500, str(e))
        return True

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