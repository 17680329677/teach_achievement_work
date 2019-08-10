import os
import easyapi
from flask import Flask, Blueprint, jsonify, send_file, request, current_app
from easyapi_tools.errors import BusinessError
from flask_jwt import jwt_required, current_identity
import app.core as controller
import app.service as service
from app.config import Config



class InnovationProjectHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.InnovationProjectController
innovation_project_bp = Blueprint(name='innovation_projects', import_name='innovation_projects', url_prefix='')
easyapi.register_api(app=innovation_project_bp, view=InnovationProjectHandler, endpoint='innovation_project_api', url='/innovation_projects')


class InnovationRankHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.InnovationRankController
innovation_rank_bp = Blueprint(name='innovation_ranks', import_name='innovation_ranks', url_prefix='')
easyapi.register_api(app=innovation_rank_bp, view=InnovationRankHandler, endpoint='innovation_rank_api', url='/innovation_ranks')



