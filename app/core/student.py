import easyapi
import app.dao as dao
from easyapi.sql import Pager, Sorter
from easyapi import EasyApiContext


class StudentController(easyapi.BaseController):
    __dao__ = dao.StudentDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 class_info 对象:
        class_info_id = res['class_info_id']
        class_info = dao.ClassInfoDao.get(ctx=ctx, query={"id": class_info_id})
        if class_info is None:
            class_info = {}
        res['class_info'] = class_info

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

            # 添加 class_info 对象:
            class_info_id = res_data['class_info_id']
            class_info = dao.ClassInfoDao.get(ctx=ctx, query={"id": class_info_id})
            if class_info is None:
                class_info = {}
            res_data['class_info'] = class_info

            # 添加 college 对象:
            college_id = res_data['college_id']
            college = dao.CollegeDao.get(ctx=ctx, query={"id": college_id})
            if college is None:
                college = {}
            res_data['college'] = college

        return res, total


class DistributionInfoController(easyapi.BaseController):
    __dao__ = dao.DistributionInfoDao

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

        return res, total


class ClassInfoController(easyapi.BaseController):
    __dao__ = dao.ClassInfoDao

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

        # 添加 distribution_info 对象:
        distribution_info_id = res['distribution_info_id']
        distribution_info = dao.DistributionInfoDao.get(ctx=ctx, query={"id": distribution_info_id})
        if distribution_info is None:
            res['distribution_info'] = {}
        else:
            res['distribution_info'] = distribution_info
            department_id = distribution_info['department_id']
            department = dao.DepartmentDao.get(ctx=ctx, query={"id": department_id})
            if department is None:
                department = {}
            res['distribution_info']['department'] = department

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

            # 添加 distribution_info 对象:
            distribution_info_id = res_data['distribution_info_id']
            distribution_info = dao.DistributionInfoDao.get(ctx=ctx, query={"id": distribution_info_id})
            if distribution_info is None:
                res_data['distribution_info'] = {}
            else:
                res_data['distribution_info'] = distribution_info
                department_id = distribution_info['department_id']
                department = dao.DepartmentDao.get(ctx=ctx, query={"id": department_id})
                if department is None:
                    department = {}
                res_data['distribution_info']['department'] = department

        return res, total

class DistributionDesireController(easyapi.BaseController):
    __dao__ = dao.DistributionDesireDao

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

        # 添加 student 对象:
        student_id = res['student_id']
        student = dao.StudentDao.get(ctx=ctx, query={"id": student_id})
        if student is None:
            student = {}
        res['student'] = student

        # 添加 distribution_info 对象:
        distribution_info_id = res['distribution_info_id']
        distribution_info = dao.DistributionInfoDao.get(ctx=ctx, query={"id": distribution_info_id})
        if distribution_info is None:
            res['distribution_info'] = {}
        else:
            res['distribution_info'] = distribution_info
            department_id = distribution_info['department_id']
            department = dao.DepartmentDao.get(ctx=ctx, query={"id": department_id})
            if department is None:
                department = {}
            res['distribution_info']['department'] = department


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

            # 添加 student 对象:
            student_id = res_data['student_id']
            student = dao.StudentDao.get(ctx=ctx, query={"id": student_id})
            if student is None:
                student = {}
            res_data['student'] = student

            # 添加 distribution_info 对象:
            distribution_info_id = res_data['distribution_info_id']
            distribution_info = dao.DistributionInfoDao.get(ctx=ctx, query={"id": distribution_info_id})
            if distribution_info is None:
                res_data['distribution_info'] = {}
            else:
                res_data['distribution_info'] = distribution_info
                department_id = distribution_info['department_id']
                department = dao.DepartmentDao.get(ctx=ctx, query={"id": department_id})
                if department is None:
                    department = {}
                res_data['distribution_info']['department'] = department

        return res, total


class DistributionResultController(easyapi.BaseController):
    __dao__ = dao.DistributionResultDao

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

        # 添加 student 对象:
        student_id = res['student_id']
        student = dao.StudentDao.get(ctx=ctx, query={"id": student_id})
        if student is None:
            student = {}
        res['student'] = student

        # 添加 distribution_info 对象:
        distribution_info_id = res['distribution_info_id']
        distribution_info = dao.DistributionInfoDao.get(ctx=ctx, query={"id": distribution_info_id})
        if distribution_info is None:
            res['distribution_info'] = {}
        else:
            res['distribution_info'] = distribution_info
            department_id = distribution_info['department_id']
            department = dao.DepartmentDao.get(ctx=ctx, query={"id": department_id})
            if department is None:
                department = {}
            res['distribution_info']['department'] = department

        # 添加 class_info 对象:
        class_info_id = res['class_info_id']
        class_info = dao.ClassInfoDao.get(ctx=ctx, query={"id": class_info_id})
        if class_info is None:
            class_info = {}
        res['class_info'] = class_info

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

            # 添加 student 对象:
            student_id = res_data['student_id']
            student = dao.StudentDao.get(ctx=ctx, query={"id": student_id})
            if student is None:
                student = {}
            res_data['student'] = student

            # 添加 distribution_info 对象:
            distribution_info_id = res_data['distribution_info_id']
            distribution_info = dao.DistributionInfoDao.get(ctx=ctx, query={"id": distribution_info_id})
            if distribution_info is None:
                res_data['distribution_info'] = {}
            else:
                res_data['distribution_info'] = distribution_info
                department_id = distribution_info['department_id']
                department = dao.DepartmentDao.get(ctx=ctx, query={"id": department_id})
                if department is None:
                    department = {}
                res_data['distribution_info']['department'] = department

            # 添加 class_info 对象:
            class_info_id = res_data['class_info_id']
            class_info = dao.ClassInfoDao.get(ctx=ctx, query={"id": class_info_id})
            if class_info is None:
                class_info = {}
            res_data['class_info'] = class_info

        return res, total
