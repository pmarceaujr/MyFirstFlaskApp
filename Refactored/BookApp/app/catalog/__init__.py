from flask import Blueprint

main = Blueprint('main', __name__, template_folder='templates', static_folder='static')
from app.catalog import routes  # to avoid circular imports
