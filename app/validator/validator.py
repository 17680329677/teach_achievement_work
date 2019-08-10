from marshmallow import Schema, fields, validates, ValidationError, post_load, validates_schema
import easyapi
import asyncio

def validate(validator, data):
    result_data, errs = validator().load(data)
    if len(errs) > 0:
        err_final = err_print("", errs)
        raise easyapi.BusinessError(code=500, http_code=200, err_info=err_final)


def err_print(header, infos):
    if type(infos) is dict:
        err_final = ""
        for key, value in infos.items():
            err_final = err_final + err_print(key, value)
        return err_final
    else:
        info_final = ""
        for info in infos:
            info_final = info_final + info
        return header + info_final + "\n"
