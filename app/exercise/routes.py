from flask import Blueprint, abort, request

from app import db
from app.exercise.models import Exercise
from app.exercise.schema import ExerciseSchema

exercise_bp = Blueprint('exercise', __name__, url_prefix='/exercise')
exercise_schema = ExerciseSchema()
exercises_schema = ExerciseSchema(many=True)


@exercise_bp.get("/")
def get_all_exercises():
    result = Exercise.query.all()
    return exercises_schema.dump(result)


@exercise_bp.get("/<exercise_id>")
def get_exercise(exercise_id):
    data = _get_exercise_by_id(exercise_id)

    if data is None:
        abort(404, description=f"Exercise ID {exercise_id} not found")
    return exercise_schema.dump(data)


@exercise_bp.post("/")
def add_exercise():
    data = exercise_schema.load(request.json)

    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return {
        "message": "Exercise created successfully",
        "data": exercise_schema.dump(data)
    }, 201


@exercise_bp.put("/<exercise_id>")
def update_exercise(exercise_id):
    data = _get_exercise_by_id(exercise_id)
    new_data = exercise_schema.load(request.json)

    data.name = new_data.name
    data.muscle_group_id = new_data.muscle_group_id

    try:
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return {
        "message": "Exercise created successfully",
        "data": exercise_schema.dump(data)
    }, 201


@exercise_bp.delete("/<exercise_id>")
def delete_exercise(exercise_id):
    data = _get_exercise_by_id(exercise_id)

    try:
        db.session.delete(data)
        db.session.commit()
    except Exception as e:
        db.session.rollback()
        raise e
    return {
        "message": "Exercise deleted successfully",
        "data": {'id': data.id, 'name': data.name}
    }, 200


def _get_exercise_by_id(exercise_id):
    data = Exercise.query.get(exercise_id)

    if data is None:
        abort(404, description=f"Exercise ID {exercise_id} not found")

    return data