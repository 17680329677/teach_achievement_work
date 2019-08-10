import os
import easyapi
from flask import Flask, Blueprint, jsonify, send_file, request, current_app
from easyapi_tools.errors import BusinessError
from flask_jwt import jwt_required, current_identity
import app.core as controller
import app.service as service
from app.config import Config




class StudentHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.StudentController
student_bp = Blueprint(name='students', import_name='students', url_prefix='')
easyapi.register_api(app=student_bp, view=StudentHandler, endpoint='student_api', url='/students')


class DistributionInfoHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.DistributionInfoController
distribution_info_bp = Blueprint(name='distribution_infos', import_name='distribution_infos', url_prefix='')
easyapi.register_api(app=distribution_info_bp, view=DistributionInfoHandler, endpoint='distribution_info_api', url='/distribution_infos')


class ClassInfoHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.ClassInfoController
class_info_bp = Blueprint(name='class_infos', import_name='class_infos', url_prefix='')
easyapi.register_api(app=class_info_bp, view=ClassInfoHandler, endpoint='class_info_api', url='/class_infos')


class DistributionDesireHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.DistributionDesireController
distribution_desire_bp = Blueprint(name='distribution_desires', import_name='distribution_desires', url_prefix='')
easyapi.register_api(app=distribution_desire_bp, view=DistributionDesireHandler, endpoint='distribution_desire_api', url='/distribution_desires')


class DistributionResultHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.DistributionResultController
distribution_result_bp = Blueprint(name='distribution_results', import_name='distribution_results', url_prefix='')
easyapi.register_api(app=distribution_result_bp, view=DistributionResultHandler, endpoint='distribution_result_api', url='/distribution_results')


