from flask import Blueprint

bp = Blueprint("casas", __name__)

from app.casas import routes
