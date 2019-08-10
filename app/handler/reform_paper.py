import os
import easyapi
from flask import Flask, Blueprint, jsonify, send_file, request, current_app
from easyapi_tools.errors import BusinessError
from flask_jwt import jwt_required, current_identity
import app.core as controller
import app.service as service
from app.config import Config

class TeachReformPaperHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.TeachReformPaperController
teach_reform_paper_bp = Blueprint(name='teach_reform_papers', import_name='teach_reform_papers', url_prefix='')
easyapi.register_api(app=teach_reform_paper_bp, view=TeachReformPaperHandler, endpoint='teach_reform_paper_api', url='/teach_reform_papers')

