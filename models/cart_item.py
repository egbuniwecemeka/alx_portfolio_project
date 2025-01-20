#!/usr/bin/python3
"""A python script that contains the CartItem class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey, Integer
from sqlalchemy.orm import relationship


class CartItem(BaseModel, Base):
    """CartItem class for linking items to carts"""
    __tablename__ = 'cart_items'

    cart_id = Column(String(60), ForeignKey('carts.id'), nullable=False)
    item_id = Column(String(60), ForeignKey('items.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)

    # Table relationships
    cart = relationship('Cart', back_populates='cart_items')
    item = relationship('Item', back_populates='cart_items')

    def __repr__(self):
        """Returns the string representation of CartItem instance"""
        return f'{self.item.name} - {self.item.price:.2f} X {self.quantity}'
    