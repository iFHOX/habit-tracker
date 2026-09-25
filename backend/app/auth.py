from flask import Blueprint

authentication_blueprint = Blueprint("auth", __name__, url_prefix="/auth")