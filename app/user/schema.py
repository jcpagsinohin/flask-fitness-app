from app import ma
from .models import AppUser


class UserSchema(ma.SQLAlchemySchema):
    class Meta:
        model = AppUser

    id = ma.auto_field()
    username = ma.auto_field()
    email = ma.auto_field()
    created_at = ma.auto_field()
    updated_at = ma.auto_field()
    sessions = ma.Nested('SessionSchema', many=True, exclude=('user',))
