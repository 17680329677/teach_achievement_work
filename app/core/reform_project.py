import easyapi
import app.dao as dao
from easyapi.sql import Pager, Sorter
from easyapi import EasyApiContext


class TeachReformProjectController(easyapi.BaseController):
    __dao__ = dao.TeachReformProjectDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 project_child_type 对象:
        project_child_type_id = res['project_child_type_id']
        project_child_type = dao.ProjectChildTypeDao.get(ctx=ctx, query={"id": project_child_type_id})
        if project_child_type is None:
            project_child_type = {}
        res['project_child_type'] = project_child_type

        # 添加 rank 对象:
        rank_id = res['rank_id']
        rank = dao.ProjectRankDao.get(ctx=ctx, query={"id": rank_id})
        if rank is None:
            rank = {}
        res['rank'] = rank

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

            # 添加 project_child_type 对象:
            project_child_type_id = res_data['project_child_type_id']
            project_child_type = dao.ProjectChildTypeDao.get(ctx=ctx, query={"id": project_child_type_id})
            if project_child_type is None:
                project_child_type = {}
            res_data['project_child_type'] = project_child_type

            # 添加 rank 对象:
            rank_id = res_data['rank_id']
            rank = dao.ProjectRankDao.get(ctx=ctx, query={"id": rank_id})
            if rank is None:
                rank = {}
            res_data['rank'] = rank

            # 添加 college 对象:
            college_id = res_data['college_id']
            college = dao.CollegeDao.get(ctx=ctx, query={"id": college_id})
            if college is None:
                college = {}
            res_data['college'] = college

        return res, total

class ProjectTypeController(easyapi.BaseController):
    __dao__ = dao.ProjectTypeDao


class ProjectChildTypeController(easyapi.BaseController):
    __dao__ = dao.ProjectChildTypeDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 project_type 对象:
        project_type_id = res['project_type_id']
        project_type = dao.ProjectTypeDao.get(ctx=ctx, query={"id": project_type_id})
        if project_type is None:
            project_type = {}
        res['project_type'] = project_type

        return res

    @classmethod
    def query(cls, ctx: EasyApiContext = None, query: dict = None, pager: Pager = None, sorter: Sorter = None, *args,
              **kwargs) -> (list, int):
        (res, total) = super().query(ctx=ctx, query=query, pager=pager, sorter=sorter)

        for res_data in res:
            # 添加 project_type 对象:
            project_type_id = res_data['project_type_id']
            project_type = dao.ProjectTypeDao.get(ctx=ctx, query={"id": project_type_id})
            if project_type is None:
                project_type = {}
            res_data['project_type'] = project_type


        return res, total



class ProjectRankController(easyapi.BaseController):
    __dao__ = dao.ProjectRankDao


class ProjectChangeRecordController(easyapi.BaseController):
    __dao__ = dao.ProjectChangeRecordDao

    @classmethod
    def get(cls, id: int, ctx: EasyApiContext = None):
        res = super().get(id)
        if res is None:
            return None

        # 添加 teach_reform_project 对象:
        teach_reform_project_id = res['teach_reform_project_id']
        teach_reform_project = dao.TeachReformProjectDao.get(ctx=ctx, query={"id": teach_reform_project_id})
        if teach_reform_project is None:
            teach_reform_project = {}
        res['teach_reform_project'] = teach_reform_project

        return res

    @classmethod
    def query(cls, ctx: EasyApiContext = None, query: dict = None, pager: Pager = None, sorter: Sorter = None, *args,
              **kwargs) -> (list, int):
        (res, total) = super().query(ctx=ctx, query=query, pager=pager, sorter=sorter)

        for res_data in res:
            # 添加 teach_reform_project 对象:
            teach_reform_project_id = res_data['teach_reform_project_id']
            teach_reform_project = dao.TeachReformProjectDao.get(ctx=ctx, query={"id": teach_reform_project_id})
            if teach_reform_project is None:
                teach_reform_project = {}
            res_data['teach_reform_project'] = teach_reform_project

        return res, total