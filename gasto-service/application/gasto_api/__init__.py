# application/gasto_api/__init__.py
from flask import Blueprint

gasto_api_blueprint = Blueprint('gasto_api', __name__)

from . import routes
