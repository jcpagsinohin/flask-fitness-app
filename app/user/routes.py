from flask import Blueprint, abort

from .models import AppUser
from .schema import UserSchema

user_bp = Blueprint('user', __name__, url_prefix='/user')
user_schema = UserSchema()
users_schema = UserSchema(many=True)


@user_bp.get("/")
def get_all_users():
    result = AppUser.query.all()
    return users_schema.dump(result)


@user_bp.get("/<user_id>")
def get_user(user_id):
    result = AppUser.query.get(user_id)

    if result is None:
        abort(404, description=f"User ID {user_id} not found")
    return user_schema.dump(result)
