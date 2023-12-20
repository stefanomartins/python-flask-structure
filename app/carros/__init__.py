from flask import Blueprint

bp = Blueprint("carros", __name__)

from app.carros import routes
