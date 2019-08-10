import os
import easyapi
from flask import Flask, Blueprint, jsonify, send_file, request, current_app
from easyapi_tools.errors import BusinessError
from flask_jwt import jwt_required, current_identity
import app.core as controller
import app.service as service
from app.config import Config


class CollegeHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.CollegeController
college_bp = Blueprint(name='colleges', import_name='colleges', url_prefix='')
easyapi.register_api(app=college_bp, view=CollegeHandler, endpoint='college_api', url='/colleges')


class DepartmentHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.DepartmentController
department_bp = Blueprint(name='departments', import_name='departments', url_prefix='')
easyapi.register_api(app=department_bp, view=DepartmentHandler, endpoint='department_api', url='/departments')


