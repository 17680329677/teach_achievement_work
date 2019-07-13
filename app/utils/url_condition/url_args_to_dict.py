import json

#handler中 get 使用

#用来吧get中问号“？”后面那部分转换成dict
#get中会有 _page  _per_page的请求 用来调整每一页的输出和分页的跳转。
#例子：'GET /:resource/:id?_expand='
def args_to_dict(condition):
    condition_fin = dict()
    for key in condition:
        for value in condition.getlist(key):
            try:
                value = json.loads(value)
            except:
                value = value
            if key not in condition_fin:
                condition_fin[key] = [value]
            else:
                condition_fin[key].append(value)
    if '_page' not in condition_fin:
        condition_fin['_page'] = [1]
    if '_per_page' not in condition_fin:
        condition_fin['_per_page'] = [20]
    return condition_fin
