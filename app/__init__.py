from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from sqlalchemy.orm import DeclarativeBase

import logging


class Base(DeclarativeBase):
    pass


app = Flask(__name__)
db = SQLAlchemy(model_class=Base)
ma = Marshmallow(app)


def create_app():
    app.config.from_object('config.DevelopmentConfig')

    # Initialize sqlAlchemy
    db.init_app(app)
    Migrate(app, db)

    # Import models
    from .musclegroup.models import MuscleGroup
    from .exercise.models import Exercise
    from .workoutset.models import WorkoutSet
    from .workoutlog.models import WorkoutLog
    from .workoutsession.models import WorkoutSession
    from .user.models import AppUser

    # Import blueprints
    from .routes import home_bp
    from .musclegroup.routes import muscle_group_bp
    from .exercise.routes import exercise_bp
    from .workoutset.routes import workout_set_bp
    from .workoutlog.routes import workout_log_bp
    from .workoutsession.routes import workout_session_bp
    from .user.routes import user_bp
    from app.common.errors import errors_bp

    # Register app blueprints
    app.register_blueprint(home_bp)
    app.register_blueprint(muscle_group_bp)
    app.register_blueprint(exercise_bp)
    app.register_blueprint(workout_set_bp)
    app.register_blueprint(workout_log_bp)
    app.register_blueprint(workout_session_bp)
    app.register_blueprint(user_bp)
    app.register_blueprint(errors_bp)

    if app.config['ENV'] == 'development':
        from scripts import seed

    with app.app_context():
        try:
            db.engine.connect()
            logging.info("Database connection successful")
        except Exception as e:
            logging.error(f"Database connection failed: {e}")
            raise

    return app
