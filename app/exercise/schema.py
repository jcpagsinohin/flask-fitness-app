from app import ma
from .models import Exercise


class ExerciseSchema(ma.SQLAlchemySchema):
    class Meta:
        model = Exercise
        load_instance = True

    id = ma.auto_field()
    name = ma.auto_field(required=True)
    muscle_group_id = ma.auto_field(required=True)
    muscle_group = ma.Function(lambda obj: obj.muscle_group.name)

