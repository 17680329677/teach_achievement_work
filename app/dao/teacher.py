import easyapi
import app.db as db


class TeacherDao(easyapi.BusinessBaseDao):
    __tablename__ = 'teachers'
    __db__ = db.mysql_db


class TeacherRoleDao(easyapi.BusinessBaseDao):
    __tablename__ = 'teacher_roles'
    __db__ = db.mysql_db


class TeacherInfoDao(easyapi.BusinessBaseDao):
    __tablename__ = 'teacher_infos'
    __db__ = db.mysql_db


class TeacherCategoryDao(easyapi.BusinessBaseDao):
    __tablename__ = 'teacher_categorys'
    __db__ = db.mysql_db


class TeacherTitleDao(easyapi.BusinessBaseDao):
    __tablename__ = 'teacher_titles'
    __db__ = db.mysql_db


class TitleRecordDao(easyapi.BusinessBaseDao):
    __tablename__ = 'title_records'
    __db__ = db.mysql_db