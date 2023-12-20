from flask import Blueprint

bp = Blueprint('houses', __name__)

from app.casas import routes