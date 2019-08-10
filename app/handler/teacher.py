import os
import easyapi
from flask import Flask, Blueprint, jsonify, send_file, request, current_app
from easyapi_tools.errors import BusinessError
from flask_jwt import jwt_required, current_identity
import app.core as controller
import app.service as service
from app.config import Config



class TeacherHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.TeacherController
teacher_bp = Blueprint(name='teachers', import_name='teachers', url_prefix='')
easyapi.register_api(app=teacher_bp, view=TeacherHandler, endpoint='teacher_api', url='/teachers')


class TeacherRoleHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.TeacherRoleController
teacher_role_bp = Blueprint(name='teacher_roles', import_name='teacher_roles', url_prefix='')
easyapi.register_api(app=teacher_role_bp, view=TeacherRoleHandler, endpoint='teacher_role_api', url='/teacher_roles')


class TeacherInfoHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.TeacherInfoController
teacher_info_bp = Blueprint(name='teacher_infos', import_name='teacher_infos', url_prefix='')
easyapi.register_api(app=teacher_info_bp, view=TeacherInfoHandler, endpoint='teacher_info_api', url='/teacher_infos')


class TeacherCategoryHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.TeacherCategoryController
teacher_category_bp = Blueprint(name='teacher_categorys', import_name='teacher_categorys', url_prefix='')
easyapi.register_api(app=teacher_category_bp, view=TeacherCategoryHandler, endpoint='teacher_category_api', url='/teacher_categorys')


class TeacherTitleHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.TeacherTitleController
teacher_title_bp = Blueprint(name='teacher_titles', import_name='teacher_titles', url_prefix='')
easyapi.register_api(app=teacher_title_bp, view=TeacherTitleHandler, endpoint='teacher_title_api', url='/teacher_titles')


class TitleRecordHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.TitleRecordController
title_record_bp = Blueprint(name='title_records', import_name='title_records', url_prefix='')
easyapi.register_api(app=title_record_bp, view=TitleRecordHandler, endpoint='title_record_api', url='/title_records')