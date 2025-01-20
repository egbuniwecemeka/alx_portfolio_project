#!/usr/bin/python3
"""A python script containg the Cart class"""

from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.cart_item import CartItem
from models.item import Item
from dotenv import load_dotenv
import models
import os

# Load env variables from .env file
load_dotenv()


class Cart(BaseModel, Base):
    """Cart class containing a user's products or items"""
    __tablename__ = 'carts'

    user_id = Column(String(60), ForeignKey('users.id'), nullable=False)
    user = relationship('User', back_populates='cart')

    # Relationship to CartItems
    cart_items = relationship('CartItem', back_populates='cart', cascade='all, delete-orphan')

    def add_item(self, item_id, quantity):
        """Adds an item to the cart"""
        for cart_item in self.cart_items:
            if cart_item.item_id == item_id:
                cart_item.quantity += quantity
                models.storage.save()
                return
        
        # Creat a new item if it doesn't exist
        new_item = CartItem(cart_id=self.id, item_id=item_id, quantity=quantity)
        self.cart_items.append(new_item)
        models.storage.new(new_item)
        models.storage.save() # Saves new item to the database
        
    def remove_item(self, item_id):
        """Removes an item from the cart"""
        item_to_del = [cart_item for cart_item in self.cart_items if cart_item.id == item_id]

        if item_to_del:
            self.cart_items.remove(item_to_del)
            models.storage.delete(item_to_del)
            models.storage.save()  # Save changes to DB

    def view_items(self):
        """List items in the cart"""
        return [str(cart_item) for cart_item in self.cart_items]
    
    def total_cost(self):
        """Calculate the total cost of items in the cart"""
        total = 0
        for cart_item in self.cart_items:
            if cart_item.item:
                print(f'CartItem: {cart_item}, Item: {cart_item.item}, Price: {cart_item.item.price}')
                total += cart_item.item.price * cart_item.quantity
            else:
                print(f'CartItem {cart_item.id} has no associated item.')
        return total
    
    def __repr__(self):
        """Returns the string representation o"""
        return f'Cart for User: {self.user_id} with {len(self.cart_items)} items'
    