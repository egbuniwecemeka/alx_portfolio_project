#!/usr/bin/python3
"""A module for my cart routes"""

from api.views import app_views
from flask import render_template, request, session, jsonify
from models import storage
from models.cart import Cart
from models.item import Item

# Route to cart
@app_views.route('/cart', methods=['GET', 'POST'], strict_slashes=False)
def cart():
    """Renders the cart HTML template"""
    return render_template('cart.html')

@app_views.route('/cart/add', methods=['POST'])
def add_to_cart():
    """"""
    data = request.json
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    cart = storage.get(cart, {'user_id': user_id})
    if not cart:
        cart = Cart(user_id=user_id)
        storage.new(cart)
    
    item_id = data.get('item_id')
    quantity = data.get('quantity', 1)
    item = storage.get(Item, item_id)

    if not item:
        return jsonify({'error': 'Item not found'}), 404
    
    cart.add_item(item_id, quantity)
    return jsonify({'message': f'{item.name} added to cart', 'cart': cart.view_items()})

# Route to Fetch the Cart
@app_views.route('/cart', methods=['GET'])
def get_cart():
    """Fetches the cart"""
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    cart = storage.get(Cart, {'user_id': user_id})
    if not cart:
        return jsonify({'message': 'Cart is empty!', 'cart': []})
    
    return jsonify({'cart': cart.view_items(), 'total_cost': cart.total_cost()})

# Route to remove an item from the cart
@app_views.route('/cart/remove', methods=['POST'])
def remove_from_cart():
    """Removes an item from the cart"""
    data = request.json
    user_id = session.get('user_id')
    if not user_id:
        return jsonify({'error': 'Unauthorized'}), 401
    
    cart = storage.get(Cart, {'user_id': user_id})
    if not cart:
        return jsonify({'message': 'Cart is empty!'})
    
    item_id = data.get('item_id')
    cart.remove_item(item_id)
    return jsonify({'message': 'Item removed from cart', 'cart': cart.view_items()})

# Route for checkout
@app_views.route('/checkout', methods=['POST'])
def checkout():
    """Checkout route"""
    user_id = session.get('user_id')
    print(f'User ID: {user_id}')
    
    if not user_id:
        return jsonify({'error': 'Unathorized'}), 401

    cart = storage.get(Cart, {'user_id': user_id})
    if not cart or not cart.cart_items:
        return jsonify({'error': 'Cart is empty!'}), 400

    #Total order
    total_cost = cart.total_cost()
    storage.delete(cart) # Empty the cart on submission

    return jsonify({'message': 'Order placed successfully', 'total': total_cost})
