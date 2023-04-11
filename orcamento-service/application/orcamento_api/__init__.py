# application/user_api/__init__.py
from . import routes
from flask import Blueprint

orcamento_api_blueprint = Blueprint('orcamento_api', __name__)
