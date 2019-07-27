import app.core.dao as dao
from app.utils import CustomError
from app import db
from datetime import datetime
from flask_login import current_user
import app.core.services as service

class BookRankController(object):
    @classmethod
    def formatter(cls, data: dict):
        return data

    @classmethod
    def reformatter_insert(cls, data: dict):
        return data

    @classmethod
    def reformatter_update(cls, data: dict):
        return data

    @classmethod
    def reformatter_query(cls, data: dict):
        return data

    @classmethod
    def get_book_rank(cls, id:int, unscoped: bool = False):
        book_rank = dao.BookRank.get_book_rank(id=id, unscoped=unscoped)
        if book_rank is None:
            raise CustomError(404, 404, '书籍类型未找到')
        return cls.formatter(book_rank)

    @classmethod
    def query_book_rank(cls, query_dict: dict, unscoped: bool = False):
        (book_ranks, num) = dao.BookRank.query_book_rank(query_dict=query_dict, unscoped=unscoped)
        return [cls.formatter(book_rank) for book_rank in book_ranks], num

    @classmethod
    def insert_book_rank(cls, ctx: bool = True, data: dict = None):
        if data is None:
            data = {}
        try:
            dao.BookRank.insert_book_rank(ctx=False, data=data)
            if ctx:
                db.session.commit()
        except Exception as e:
            if ctx:
                db.session.rollback()
            if isinstance(e, CustomError):
                raise e
            else:
                raise CustomError(500, 200, str(e))
        return True

    @classmethod
    def update_book_rank(cls, ctx: bool = True, id: int = 0, data: dict = None):
        if data is None:
            data = {}
        data = cls.reformatter_update(data)
        book_rank = dao.BookRank.get_book_rank(id=id, unscoped=False)
        if book_rank is None:
            raise CustomError(404, 404, "书籍类型未找到")
        try:
            dao.BookRank.update_book_rank(ctx=False, query_dict={'id':[id]},data=data)
            if ctx:
                db.session.commit()
        except Exception as e:
            if ctx:
                db.session.rollback()
            if isinstance(e, CustomError):
                raise e
            else:
                raise CustomError(500, 500, str(e))
        return True

    @classmethod
    def delete_book_rank(cls, ctx: bool = True, id: int = 0):
        book_rank = dao.BookRank.get_book_rank(id=id, unscoped=False)
        if book_rank is None:
            return CustomError(404, 404, "书籍类型未找到")
        try:
            dao.BookRank.delete_book_rank(ctx=False,query_dict={'id': [id]})
            if ctx:
                db.session.commit()
        except Exception as e:
            if ctx:
                db.session.rollback()
            if isinstance(e, CustomError):
                raise e
            else:
                raise CustomError(500, 500, str(e))
        return True



