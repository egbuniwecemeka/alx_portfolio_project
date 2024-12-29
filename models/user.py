from models.base_model import BaseModel, Base
from models.place import Place
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

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
    places = relationship('Place', cascade=['all', 'delete-orphan'],
                          backref='user')
    reviews = relationship('Reviews', cascade=['all', 'delete-orphan'],
                           backref='user')
