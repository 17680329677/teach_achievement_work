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
        newdata = dict()

        # **********************

        return newdata


    @classmethod
    def reformatter_query(cls, data: dict):
        return data

    @classmethod
    def insert_book_rank(cls, ctx: bool = True, data: dict = None):
        if data is None:
            data = {}


        # **********************
        return True