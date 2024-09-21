from sqlalchemy import Integer, String, DateTime, Numeric, ForeignKey, func
from sqlalchemy.orm import mapped_column, relationship

from app import db


class WorkoutSet(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    workout_log_id = mapped_column(Integer, ForeignKey('workout_log.id'))
    exercise_id = mapped_column(Integer, ForeignKey('exercise.id'), nullable=False)
    reps = mapped_column(Integer, nullable=False)
    set_number = mapped_column(Integer, nullable=False)
    weight_kg = mapped_column(Numeric(4, 2), nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())

    exercise = relationship('Exercise')
    workout_log = relationship('WorkoutLog', back_populates='workout_sets')
