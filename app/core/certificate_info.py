import easyapi
import app.dao as dao
from easyapi.sql import Pager, Sorter
from easyapi import EasyApiContext



class CertificateInfoController(easyapi.BaseController):
    __dao__ = dao.CertificateInfoDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 rank 对象:
        rank_id = res['rank_id']
        rank = dao.CertificateRankDao.get(ctx=ctx, query={"id": rank_id})
        if rank is None:
            rank = {}
        res['rank'] = rank

        # 添加 college 对象:
        college_id = res['college_id']
        college = dao.CollegeDao.get(ctx=ctx, query={"id": college_id})
        if college is None:
            college = {}
        res['college'] = college

        # 添加 teacher 对象:
        teacher_id = res['teacher_id']
        teacher = dao.TeacherDao.get(ctx=ctx, query={"id": teacher_id})
        if teacher is None:
            teacher = {}
        else:
            teacher_info_id = teacher['teacher_info_id']
            teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
            if teacher_info is None:
                teacher_info = {}
            res['teacher']['teacher_info'] = teacher_info
        res['teacher'] = teacher

        return res

    @classmethod
    def query(cls, ctx: EasyApiContext = None, query: dict = None, pager: Pager = None, sorter: Sorter = None, *args,
              **kwargs) -> (list, int):
        (res, total) = super().query(ctx=ctx, query=query, pager=pager, sorter=sorter)
        for res_data in res:
            # 添加 rank 对象:
            rank_id = res_data['rank_id']
            rank = dao.BookRankDao.get(ctx=ctx, query={"id": rank_id})
            if rank is None:
                rank = {}
            res_data['rank'] = rank

            # 添加 college 对象:
            college_id = res_data['college_id']
            college = dao.CollegeDao.get(ctx=ctx, query={"id": college_id})
            if college is None:
                college = {}
            res_data['college'] = college

            # 添加 teacher 对象:
            teacher_id = res_data['teacher_id']
            teacher = dao.TeacherDao.get(ctx=ctx, query={"id": teacher_id})
            if teacher is None:
                teacher = {}
            else:
                teacher_info_id = teacher['teacher_info_id']
                teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
                if teacher_info is None:
                    teacher_info = {}
                    res_data['teacher']['teacher_info'] = teacher_info
                res_data['teacher'] = teacher

        return res, total



class CertificateRankController(easyapi.BaseController):
    __dao__ = dao.CertificateRankDao


