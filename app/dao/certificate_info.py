import easyapi
import app.db as db


class CertificateInfoDao(easyapi.BusinessBaseDao):
    __tablename__ = 'certificate_infos'
    __db__ = db.mysql_db


class CertificateRankDao(easyapi.BusinessBaseDao):
    __tablename__ = 'certificate_ranks'
    __db__ = db.mysql_db