from flask import Blueprint

habits_blueprint = Blueprint("habits", __name__, url_prefix="/habits")