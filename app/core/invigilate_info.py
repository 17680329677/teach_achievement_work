import easyapi
import app.dao as dao
from easyapi.sql import Pager, Sorter
from easyapi import EasyApiContext


class InvigilateInfoController(easyapi.BaseController):
    __dao__ = dao.InvigilateInfoDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 apply_teacher 对象:
        apply_teacher_id = res['apply_teacher_id']
        apply_teacher = dao.TeacherDao.get(ctx=ctx, query={"id": apply_teacher_id})
        if apply_teacher is None:
            apply_teacher = {}
        else:
            teacher_info_id = apply_teacher['teacher_info_id']
            teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
            if teacher_info is None:
                teacher_info = {}
            res['apply_teacher']['teacher_info'] = teacher_info
        res['apply_teacher'] = apply_teacher

        # 添加 semester_info 对象:
        semester_info_id = res['semester_info_id']
        semester_info = dao.SemesterInfoDao.get(ctx=ctx, query={"id": semester_info_id})
        if semester_info is None:
            semester_info = {}
        res['semester_info'] = semester_info

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
            # 添加 apply_teacher 对象:
            apply_teacher_id = res_data['apply_teacher_id']
            apply_teacher = dao.TeacherDao.get(ctx=ctx, query={"id": apply_teacher_id})
            if apply_teacher is None:
                apply_teacher = {}
            else:
                teacher_info_id = apply_teacher['teacher_info_id']
                teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
                if teacher_info is None:
                    teacher_info = {}
                res_data['apply_teacher']['teacher_info'] = teacher_info
            res_data['apply_teacher'] = apply_teacher

            # 添加 semester_info 对象:
            semester_info_id = res_data['semester_info_id']
            semester_info = dao.SemesterInfoDao.get(ctx=ctx, query={"id": semester_info_id})
            if semester_info is None:
                semester_info = {}
            res['semester_info'] = semester_info

            # 添加 college 对象:
            college_id = res_data['college_id']
            college = dao.CollegeDao.get(ctx=ctx, query={"id": college_id})
            if college is None:
                college = {}
            res_data['college'] = college

        return res, total


class SemesterInfoController(easyapi.BaseController):
    __dao__ = dao.SemesterInfoDao


class CourseController(easyapi.BaseController):
    __dao__ = dao.CourseDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

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
            # 添加 college 对象:
            college_id = res_data['college_id']
            college = dao.CollegeDao.get(ctx=ctx, query={"id": college_id})
            if college is None:
                college = {}
            res_data['college'] = college

        return res, total