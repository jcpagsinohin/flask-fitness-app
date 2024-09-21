from flask import Blueprint, abort

from .models import WorkoutSession
from .schema import WorkoutSessionSchema

workout_session_bp = Blueprint('workoutsession', __name__, url_prefix='/workout-workoutsession')
workout_sessions_schema = WorkoutSessionSchema(many=True)


@workout_session_bp.get("/")
def get_all_workout_sessions():
    result = WorkoutSession.query.all()
    return workout_sessions_schema.dump(result)