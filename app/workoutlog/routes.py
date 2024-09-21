from flask import Blueprint, abort

from .models import WorkoutLog

workout_log_bp = Blueprint('workout_log', __name__, url_prefix='/workout-log')


@workout_log_bp.get("/")
def get_all_workout_logs():
    result = WorkoutLog.query.all()
    return [item.as_dict() for item in result]