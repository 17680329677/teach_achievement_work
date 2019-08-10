import easyapi
import app.db as db

class BookDao(easyapi.BusinessBaseDao):
    __tablename__ = 'books'
    __db__ = db.mysql_db


class BookRankDao(easyapi.BusinessBaseDao):
    __tablename__ = 'book_ranks'
    __db__ = db.mysql_db