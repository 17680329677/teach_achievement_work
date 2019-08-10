import os
import easyapi
from flask import Flask, Blueprint, jsonify, send_file, request, current_app
from easyapi_tools.errors import BusinessError
from flask_jwt import jwt_required, current_identity
import app.core as controller
import app.service as service
from app.config import Config


class CertificateInfoHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.CertificateInfoController
certificate_info_bp = Blueprint(name='certificate_infos', import_name='certificate_infos', url_prefix='')
easyapi.register_api(app=certificate_info_bp, view=CertificateInfoHandler, endpoint='certificate_info_api', url='/certificate_infos')


class CertificateRankHandler(easyapi.FlaskBaseHandler):
    __controller__ = controller.CertificateRankController
certificate_rank_bp = Blueprint(name='certificate_ranks', import_name='certificate_ranks', url_prefix='')
easyapi.register_api(app=certificate_rank_bp, view=CertificateRankHandler, endpoint='certificate_rank_api', url='/certificate_ranks')



