from models.base_model import BaseModel, Base
from sqlalchemy import Column, String
from sqlalchemy.orm import relationship

class User(BaseModel, Base):
    """User class that inherits from BaseModel
        It represents a user with email, password, first_name and last_name
    """
    __tablename__ = 'users'
    # Public attribute
    username = Column(String(128), nullable=False)
    email = Column(String(128), nullable=False)
    password = Column(String(225), nullable=False)
    first_name = Column(String(128), nullable=True)
    last_name = Column(String(128), nullable=True)
    places = relationship('Place', cascade=['all', 'delete-orphan'],
                          backref='user')
    reviews = relationship('Review', cascade=['all', 'delete-orphan'],
                           backref='user')
    cart = relationship('Cart', uselist=False, cascade=['all', 'delete-orphan'],
                        back_populates='user')

