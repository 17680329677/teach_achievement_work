import os
import easyapi
from flask import Flask, Blueprint, jsonify, send_file, request, current_app
from easyapi_tools.errors import BusinessError
from flask_jwt import jwt_required, current_identity
import app.core as controller
import app.service as service
from app.config import Config



class InvigilateInfoHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.InvigilateInfoController
invigilate_info_bp = Blueprint(name='invigilate_infos', import_name='invigilate_infos', url_prefix='')
easyapi.register_api(app=invigilate_info_bp, view=InvigilateInfoHandler, endpoint='invigilate_info_api', url='/invigilate_infos')


class SemesterInfoHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.SemesterInfoController
semester_info_bp = Blueprint(name='semester_infos', import_name='semester_infos', url_prefix='')
easyapi.register_api(app=semester_info_bp, view=SemesterInfoHandler, endpoint='semester_info_api', url='/semester_infos')


class CourseHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.CourseController
course_bp = Blueprint(name='courses', import_name='courses', url_prefix='')
easyapi.register_api(app=course_bp, view=CourseHandler, endpoint='course_api', url='/courses')



