import os
import easyapi
from flask import Flask, Blueprint, jsonify, send_file, request, current_app
from easyapi_tools.errors import BusinessError
from flask_jwt import jwt_required, current_identity
import app.core as controller
import app.service as service
from app.config import Config



class TeachReformProjectHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.TeachReformProjectController
teach_reform_project_bp = Blueprint(name='teach_reform_projects', import_name='teach_reform_projects', url_prefix='')
easyapi.register_api(app=teach_reform_project_bp, view=TeachReformProjectHandler, endpoint='teach_reform_project_api', url='/teach_reform_projects')


class ProjectTypeHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.ProjectTypeController
project_type_bp = Blueprint(name='project_types', import_name='project_types', url_prefix='')
easyapi.register_api(app=project_type_bp, view=ProjectTypeHandler, endpoint='project_type_api', url='/project_types')


class ProjectChildTypeHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.ProjectChildTypeController
project_child_type_bp = Blueprint(name='project_child_types', import_name='project_child_types', url_prefix='')
easyapi.register_api(app=project_child_type_bp, view=ProjectChildTypeHandler, endpoint='project_child_type_api', url='/project_child_types')


class ProjectRankHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.ProjectRankController
project_rank_bp = Blueprint(name='project_ranks', import_name='project_ranks', url_prefix='')
easyapi.register_api(app=project_rank_bp, view=ProjectRankHandler, endpoint='project_rank_api', url='/project_ranks')


class ProjectChangeRecordHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.ProjectChangeRecordController
project_change_record_bp = Blueprint(name='project_change_records', import_name='project_change_records', url_prefix='')
easyapi.register_api(app=project_change_record_bp, view=ProjectChangeRecordHandler, endpoint='project_change_record_api', url='/project_change_records')


