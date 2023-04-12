# application/orcamento_api/__init__.py
from flask import Blueprint

orcamento_api_blueprint = Blueprint('orcamento_api', __name__)

from . import routes
