#!/usr/bin/python3
"""A python script containing the Item class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, Float
from sqlalchemy.orm import relationship


class Item(BaseModel, Base):
    """Represents an item in the cart"""
    __tablename__ = 'items'

    name = Column(String(128), nullable=False)
    price = Column(Float, nullable=False)

    # Relationship to CartItems
    cart_items = relationship('CartItem', back_populates='item')
    
    def __repr__(self):
        """Returns a string representation of an item"""
        return f'Item: {self.name} - ${self.price:.2f}'
