from flask import Blueprint, abort

from .models import MuscleGroup
from .schema import MuscleGroupSchema

muscle_group_bp = Blueprint('muscle_group', __name__, url_prefix='/muscle-group')
muscle_group_schema = MuscleGroupSchema(many=True)


@muscle_group_bp.get("/")
def get_all_muscle_groups():
    result = MuscleGroup.query.all()
    return muscle_group_schema.dump(result)