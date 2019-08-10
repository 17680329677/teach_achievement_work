import easyapi
import app.dao as dao
from easyapi.sql import Pager, Sorter
from easyapi import EasyApiContext

class TeachReformPaperController(easyapi.BaseController):
    __dao__ = dao.TeachReformPaperDao

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