import easyapi
import app.db as db


class StudentDao(easyapi.BusinessBaseDao):
    __tablename__ = 'students'
    __db__ = db.mysql_db


class DistributionInfoDao(easyapi.BusinessBaseDao):
    __tablename__ = 'distribution_infos'
    __db__ = db.mysql_db


class ClassInfoDao(easyapi.BusinessBaseDao):
    __tablename__ = 'class_infos'
    __db__ = db.mysql_db


class DistributionDesireDao(easyapi.BusinessBaseDao):
    __tablename__ = 'distribution_desires'
    __db__ = db.mysql_db


class DistributionResultDao(easyapi.BusinessBaseDao):
    __tablename__ = 'distribution_results'
    __db__ = db.mysql_db