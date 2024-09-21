from sqlalchemy import Integer, String, ForeignKey
from sqlalchemy.orm import mapped_column, relationship

from app import db


class Exercise(db.Model):
    id = mapped_column(Integer, primary_key=True, autoincrement=True)
    name = mapped_column(String, nullable=False)
    muscle_group_id = mapped_column(Integer, ForeignKey('muscle_group.id'))

    muscle_group = relationship('MuscleGroup', back_populates='exercises')
