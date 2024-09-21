from flask import Blueprint, abort

from .models import WorkoutSet

workout_set_bp = Blueprint('workout_set', __name__, url_prefix='/workout-set')


@workout_set_bp.get("/")
def get_all_workout_set():
    result = WorkoutSet.query.all()
    return [item.as_dict() for item in result]