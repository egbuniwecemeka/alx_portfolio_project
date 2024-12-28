from models.base_model import BaseModel, Base
from sqlalchemy import Column, String

class User(BaseModel, Base):
    """User class that inherits from BaseModel
        It represents a user with email, password, first_name and last_name
    """
    __tablename__ = 'users'
    # Public attribute
    email = Column(String(128), nullable=False)
    password = Column(String(128), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
