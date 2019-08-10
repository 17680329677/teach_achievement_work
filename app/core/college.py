import easyapi
import app.dao as dao
from easyapi.sql import Pager, Sorter
from easyapi import EasyApiContext

class CollegeController(easyapi.BaseController):
    __dao__ = dao.CollegeDao


class DepartmentController(easyapi.BaseController):
    __dao__ = dao.DepartmentDao


    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 director_teacher 对象:
        director_teacher_id = res['director_teacher_id']
        director_teacher = dao.TeacherDao.get(ctx=ctx, query={"id": director_teacher_id})
        if director_teacher is None:
            director_teacher = {}
        else:
            teacher_info_id = director_teacher['teacher_info_id']
            teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
            if teacher_info is None:
                teacher_info = {}
            res['director_teacher']['teacher_info'] = teacher_info
        res['director_teacher'] = director_teacher

        # 添加 college 对象:
        college_id = res['college_id']
        college = dao.CollegeDao.get(ctx=ctx, query={"id": college_id})
        if college is None:
            college = {}
        res['college'] = college

        return res

    @classmethod
    def query(cls, ctx: EasyApiContext = None, query: dict = None, pager: Pager = None, sorter: Sorter = None, *args,
              **kwargs) -> (list, int):
        (res, total) = super().query(ctx=ctx, query=query, pager=pager, sorter=sorter)

        for res_data in res:
            # 添加 director_teacher 对象:
            director_teacher_id = res_data['director_teacher_id']
            director_teacher = dao.TeacherDao.get(ctx=ctx, query={"id": director_teacher_id})
            if director_teacher is None:
                director_teacher = {}
            else:
                teacher_info_id = director_teacher['teacher_info_id']
                teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
                if teacher_info is None:
                    teacher_info = {}
                res_data['director_teacher']['teacher_info'] = teacher_info
            res_data['director_teacher'] = director_teacher

            # 添加 college 对象:
            college_id = res_data['college_id']
            college = dao.CollegeDao.get(ctx=ctx, query={"id": college_id})
            if college is None:
                college = {}
            res_data['college'] = college

        return res, total