from sqlalchemy import Integer, String, DateTime, func
from sqlalchemy.orm import mapped_column, relationship

from app import db


class AppUser(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    username = mapped_column(String(30), nullable=False, unique=True)
    email = mapped_column(String, nullable=False)
    created_at = mapped_column(DateTime, nullable=False, default=func.now())
    updated_at = mapped_column(DateTime, nullable=False, default=func.now())

    workout_sessions = relationship('WorkoutSession', back_populates='user')