import easyapi
import app.db as db


class InvigilateInfoDao(easyapi.BusinessBaseDao):
    __tablename__ = 'invigilate_infos'
    __db__ = db.mysql_db


class SemesterInfoDao(easyapi.BusinessBaseDao):
    __tablename__ = 'semester_infos'
    __db__ = db.mysql_db


class CourseDao(easyapi.BusinessBaseDao):
    __tablename__ = 'courses'
    __db__ = db.mysql_db