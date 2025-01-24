#!/usr/bin/python3
"""Question module"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Integer

class Question(BaseModel, Base):
    """Question class"""
    __tablename__ = 'questions'

    # Fields for the question model
    question = Column(String(200), nullable=False)
    option_1 = Column(String(100), nullable=False)
    option_2 = Column(String(100), nullable=False)
    option_3 = Column(String(100), nullable=False)
    option_4 = Column(String(100), nullable=False)
    correct_option = Column(Integer, nullable=False)
