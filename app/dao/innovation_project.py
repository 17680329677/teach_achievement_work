import easyapi
import app.db as db


class InnovationProjectDao(easyapi.BusinessBaseDao):
    __tablename__ = 'innovation_projects'
    __db__ = db.mysql_db


class InnovationRankDao(easyapi.BusinessBaseDao):
    __tablename__ = 'innovation_ranks'
    __db__ = db.mysql_db


