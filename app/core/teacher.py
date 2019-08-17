import easyapi
import app.dao as dao
from easyapi.sql import Pager, Sorter
from easyapi import EasyApiContext


class TeacherController(easyapi.BaseController):
    __dao__ = dao.TeacherDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 teacher_info 对象:
        teacher_info_id = res['teacher_info_id']
        teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
        if teacher_info is None:
            teacher_info = {}
        res['teacher_info'] = teacher_info

        return res

    @classmethod
    def query(cls, ctx: EasyApiContext = None, query: dict = None, pager: Pager = None, sorter: Sorter = None, *args,
              **kwargs) -> (list, int):
        (res, total) = super().query(ctx=ctx, query=query, pager=pager, sorter=sorter)

        for res_data in res:
            # 添加 teacher_info 对象:
            teacher_info_id = res_data['teacher_info_id']
            teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
            if teacher_info is None:
                teacher_info = {}
            res_data['teacher_info'] = teacher_info

        return res, total


class TeacherRoleController(easyapi.BaseController):
    __dao__ = dao.TeacherRoleDao


class TeacherInfoController(easyapi.BaseController):
    __dao__ = dao.TeacherInfoDao

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

        # 添加 department 对象:
        department_id = res['department_id']
        department = dao.DepartmentDao.get(ctx=ctx, query={"id": department_id})
        if department is None:
            department = {}
        res['department'] = department

        # 添加 [教学职称]teacher_title 对象, 这里teacher_title是教学职称
        teacher_title_id = res['teacher_title_id']
        teacher_title = dao.TeacherTitleDao.get(ctx=ctx, query={"id": teacher_title_id})
        if teacher_title is None:
            teacher_title = {}
        res['teach_title'] = teacher_title

        # 添加 [管理职称]teacher_title 对象, 这里teacher_title是管理职称
        manager_title_id = res['manager_title_id']
        teacher_title = dao.TeacherTitleDao.get(ctx=ctx, query={"id": manager_title_id})
        if teacher_title is None:
            teacher_title = {}
        res['manage_title'] = teacher_title

        # 添加 teacher_role 对象:
        teacher_role_id = res['teacher_role_id']
        teacher_role = dao.TeacherRoleDao.get(ctx=ctx, query={"id": teacher_role_id})
        if teacher_role is None:
            teacher_role = {}
        res['teacher_role'] = teacher_role

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

            # 添加 department 对象:
            department_id = res_data['department_id']
            department = dao.DepartmentDao.get(ctx=ctx, query={"id": department_id})
            if department is None:
                department = {}
            res_data['department'] = department

            # 添加 [教学职称]teacher_title 对象, 这里teacher_title是教学职称
            teacher_title_id = res_data['teacher_title_id']
            teacher_title = dao.TeacherTitleDao.get(ctx=ctx, query={"id": teacher_title_id})
            if teacher_title is None:
                teacher_title = {}
            res_data['teach_title'] = teacher_title

            # 添加 [管理职称]teacher_title 对象, 这里teacher_title是管理职称
            manager_title_id = res_data['manager_title_id']
            teacher_title = dao.TeacherTitleDao.get(ctx=ctx, query={"id": manager_title_id})
            if teacher_title is None:
                teacher_title = {}
            res_data['manage_title'] = teacher_title

            # 添加 teacher_role 对象:
            teacher_role_id = res_data['teacher_role_id']
            teacher_role = dao.TeacherRoleDao.get(ctx=ctx, query={"id": teacher_role_id})
            if teacher_role is None:
                teacher_role = {}
            res_data['teacher_role'] = teacher_role

        return res, total



class TeacherCategoryController(easyapi.BaseController):
    __dao__ = dao.TeacherCategoryDao


class TeacherTitleController(easyapi.BaseController):
    __dao__ = dao.TeacherTitleDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 teacher_category 对象:
        teacher_category_id = res['teacher_category_id']
        teacher_category = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_category_id})
        if teacher_category is None:
            teacher_category = {}
        res['teacher_category'] = teacher_category

        return res

    @classmethod
    def query(cls, ctx: EasyApiContext = None, query: dict = None, pager: Pager = None, sorter: Sorter = None, *args,
              **kwargs) -> (list, int):
        (res, total) = super().query(ctx=ctx, query=query, pager=pager, sorter=sorter)

        for res_data in res:
            # 添加 teacher_category 对象:
            teacher_category_id = res_data['teacher_category_id']
            teacher_category = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_category_id})
            if teacher_category is None:
                teacher_category = {}
            res_data['teacher_category'] = teacher_category

        return res, total


class TitleRecordController(easyapi.BaseController):
    __dao__ = dao.TitleRecordDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 teacher 对象:
        teacher_id = res['teacher_id']
        teacher = dao.TeacherDao.get(ctx=ctx, query={"id": teacher_id})
        if teacher is None:
            res['teacher'] = {}
        else:
            res['teacher'] = teacher
            teacher_info_id = teacher['teacher_info_id']
            teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
            if teacher_info is None:
                teacher_info = {}
            res['teacher']['teacher_info'] = teacher_info

        # 添加 teacher_title 对象, 这里teacher_title是 教学职称/管理职称 都有可能
        teacher_title_id = res['teacher_title_id']
        teacher_title = dao.TeacherTitleDao.get(ctx=ctx, query={"id": teacher_title_id})
        if teacher_title is None:
            teacher_title = {}
        res['teacher_title'] = teacher_title

        return res

    @classmethod
    def query(cls, ctx: EasyApiContext = None, query: dict = None, pager: Pager = None, sorter: Sorter = None, *args,
              **kwargs) -> (list, int):
        (res, total) = super().query(ctx=ctx, query=query, pager=pager, sorter=sorter)

        for res_data in res:
            # 添加 teacher 对象:
            teacher_id = res['teacher_id']
            teacher = dao.TeacherDao.get(ctx=ctx, query={"id": teacher_id})
            if teacher is None:
                res_data['teacher'] = {}
            else:
                res_data['teacher'] = teacher
                teacher_info_id = teacher['teacher_info_id']
                teacher_info = dao.TeacherInfoDao.get(ctx=ctx, query={"id": teacher_info_id})
                if teacher_info is None:
                    teacher_info = {}
                res_data['teacher']['teacher_info'] = teacher_info

            # 添加 teacher_title 对象, 这里teacher_title是 教学职称/管理职称 都有可能
            teacher_title_id = res_data['teacher_title_id']
            teacher_title = dao.TeacherTitleDao.get(ctx=ctx, query={"id": teacher_title_id})
            if teacher_title is None:
                teacher_title = {}
            res_data['teacher_title'] = teacher_title

        return res, total