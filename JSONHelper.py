"""
    配合多表查询将查询结果list转换为json
"""


class JSONHelper():
    @staticmethod
    def jsonBQlist(bqlist):
        result=[]
        for item in bqlist:
            jsondata={}
            for i in range(item.__len__()):
                tdic={item._fields[i]:item[i]}
                jsondata.update(tdic)
            result.append(jsondata)
        return result
