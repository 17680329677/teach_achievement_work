import easyapi
import app.db as db


class TeachReformPaperDao(easyapi.BusinessBaseDao):
    __tablename__ = 'teach_reform_papers'
    __db__ = db.mysql_db
