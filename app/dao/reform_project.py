import easyapi
import app.db as db


class TeachReformProjectDao(easyapi.BusinessBaseDao):
    __tablename__ = 'teach_reform_projects'
    __db__ = db.mysql_db


class ProjectTypeDao(easyapi.BusinessBaseDao):
    __tablename__ = 'project_types'
    __db__ = db.mysql_db


class ProjectChildTypeDao(easyapi.BusinessBaseDao):
    __tablename__ = 'project_child_types'
    __db__ = db.mysql_db


class ProjectRankDao(easyapi.BusinessBaseDao):
    __tablename__ = 'project_ranks'
    __db__ = db.mysql_db


class ProjectChangeRecordDao(easyapi.BusinessBaseDao):
    __tablename__ = 'project_change_records'
    __db__ = db.mysql_db