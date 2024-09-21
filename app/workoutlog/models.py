from sqlalchemy import Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column, relationship

from app import db


class WorkoutLog(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    workout_session_id = mapped_column(Integer, ForeignKey('workout_session.id'))
    exercise_id = mapped_column(Integer, ForeignKey('exercise.id'))
    sets = mapped_column(Integer, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())

    workout_session = relationship('WorkoutSession', back_populates='workout_logs')
    workout_sets = relationship('WorkoutSet', back_populates='workout_log')