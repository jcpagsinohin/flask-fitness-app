from sqlalchemy import Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import mapped_column, relationship

from app import db


class WorkoutSession(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    user_id = mapped_column(Integer, ForeignKey('app_user.id'))
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    ended_at = mapped_column(DateTime, nullable=False)

    user = relationship('AppUser', back_populates='workout_sessions')
    workout_logs = relationship('WorkoutLog', back_populates='workout_session')