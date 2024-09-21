from app import ma
from .models import WorkoutSession


class WorkoutSessionSchema(ma.SQLAlchemySchema):
    class Meta:
        model = WorkoutSession

    id = ma.auto_field()
    user_id = ma.auto_field()
    created_at = ma.auto_field()
    ended_at = ma.auto_field()
    user = ma.Nested('UserSchema', exclude=('sessions',))