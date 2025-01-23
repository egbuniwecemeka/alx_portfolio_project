from models import storage
from models.user import User
from models.cart import Cart
from models.item import Item

# Reload the storage system ensuring tables/objects are loaded
storage.reload()

# Create a user
user = User(username='test_user', email="test@example.com", password="securepass")
user.save()

# Create a cart for the user
cart = Cart(user_id=user.id)
cart.save()

# Add items to the cart
item1 = Item(name="Broiler", price=35000)
item1.save()
item2 = Item(name="Turkey", price=50000)
item2.save()

cart.add_item(item1.id, 2)
cart.add_item(item2.id, 3)

# View cart details
print(cart.view_items())
print(f"Total cost: {cart.total_cost()}")
