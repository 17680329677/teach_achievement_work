import app.core.dao as dao
from app.utils import CustomError
from app import db
from datetime import datetime
from flask_login import current_user
import app.core.services as service

class BookRankController(object):
    @classmethod
    def formatter(cls, book_rank: dict):
        return book_rank

    @classmethod
    def reformatter(cls, data: dict):
        #newdata = dict()
        return data

    @classmethod
    def reformatter_query(cls, data: dict):
        return data

    @classmethod
    def insert_book_rank(cls, ctx: bool = True, data: dict = None):
        if data is None:
            data = {}

        if 1 :
            raise CustomError(500, 200, "名称已存在")
        data = cls.reformatter(data)
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
                raise CustomError(500, 200)

        # **********************
        return True


    @classmethod
    def update_book_rank(cls, ctx: bool = True, id: int = 0, data: dict = None):
        if data is None:
            data = {}

        # **********************
        return True

    @classmethod
    def delete_book_rank(cls, ctx: bool = True, id: int = True):
        # **********************
        return True



