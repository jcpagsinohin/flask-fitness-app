from flask import Blueprint

home_bp = Blueprint('home', __name__)


@home_bp.get("/")
def home():
    return "<p>Fitness app</p>"
