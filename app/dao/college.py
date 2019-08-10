import easyapi
import app.db as db


class CollegeDao(easyapi.BusinessBaseDao):
    __tablename__ = 'colleges'
    __db__ = db.mysql_db


class DepartmentDao(easyapi.BusinessBaseDao):
    __tablename__ = 'departments'
    __db__ = db.mysql_db