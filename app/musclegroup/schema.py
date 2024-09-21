from app import ma
from .models import MuscleGroup


class MuscleGroupSchema(ma.SQLAlchemySchema):
    class Meta:
        model = MuscleGroup

    id = ma.auto_field()
    name = ma.auto_field()
    exercises = ma.Nested('ExerciseSchema', many=True, exclude=('muscle_group',))

