const products = [
    { id: 1, name: "Broiler Chick", price: 1000 },
    { id: 2, name: "Turkey", price: 2500 },
    { id: 3, name: "Peacock", price: 8000 },
    { id: 4, name: "Dog", price: 5000 }
];

let cart = JSON.parse(localStorage.getItem('cart')) || [];

//Load products into the Cart list
function loadProducts() {
    const prodList = document.getElementById('product-list');
    products.forEach(product => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${product.name} - ₦${product.price}</span>
            <input type="number" id="quantity-${product.id}" value="1" min="1" style="width: 50px;">
            <button onclick="addCartItem(${product.id})">Add to cart</button>
        `;
        prodList.appendChild(li);        
    });
}

// Add items  to cart
function addCartItem(prodId) {
    const product = products.find(prod => prod.id === prodId);
    const quantityVal = document.getElementById(`quantity-${product.id}`);
    const quantity = parseInt(quantityVal.value);

    if (quantity < 1) {
        alert('Quantity must be at least 1.');
        return;
    }

    const existingItem = cart.find(item => item.id === prodId);

    if (existingItem) {
        existingItem.quantity += quantity;
    } else {
        cart.push({ ...product, quantity });
    }

    updateCartItem()
    totalPrice();
    saveCart();
}
 
//Update cart items
function updateCartItem() {
    const cartList = document.getElementById('cart-list');
    cartList.innerHTML = ``;    //Clears cart

    cart.forEach(item => {
        const li = document.createElement('li');
        li.innerHTML = `
            <span>${item.name} - ₦${item.price} x ${item.quantity}</span>
            <button onclick="removeCartItem(${item.id})">Remove</button>
        `;
        cartList.appendChild(li);
    });

    updateCartCount();
}

// Remove item from cart
function removeCartItem(productId) {
    cart = cart.filter(item => item.id !== productId);
    updateCartItem();
    totalPrice();
    saveCart();
}

//Saves cart to local storage
function saveCart() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Update the cart count
function updateCartCount() {
    cartCount = document.getElementById('cart-count');
    const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
    cartCount.textContent = totalItems;
}

// Update total price
function totalPrice() {
    const total = cart.reduce((sum, item) => sum + item.price * item.quantity, 0);
    const totalElement = document.getElementById('total-price');
    totalElement.textContent = `Total: ₦${total}`;
}
// Simulate checkout
function checkout() {
    if (cart.length === 0) {
        alert("Your cart is empty.");
        return;
    }

    // Send cart data to the backend
    fetch('/checkout', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ cart }), // Send cart data as JSON
    })
    .then(response => {
        if (!response.ok) {
            throw new Error('Cart Items not updated to database');
        }
        return response.json();
    })
    .then(data => {
        alert(data.message);
        cart = [];
        updateCartItem();
        totalPrice();
        saveCart();
    })
    .catch(error =>{
        console.error(error);
        alert('Error, checkout failed!')
    });

    alert("Thank you for shopping with us.");
    cart = [];
    updateCartItem();
    totalPrice();
    saveCart();
}

// Load cart items on page load
document.addEventListener('DOMContentLoaded', () => {
    loadProducts();
    updateCartItem();
    totalPrice();
})

/* global $ */
$(document).ready(() => {
    $('.darkmode').click(function() {
        if ($('body').hasClass('dark')) {
            /* revert it back to normal mode */
            $('body').removeClass('dark');
            $('body').css('background-color', 'rgb(224, 217, 217)');
            $('h1, h2').css('color', '#000000');
            $('.darkmode').text('Dark Mode');
        } else {
            /* switch to dark mode */
            $('body').addClass('dark');
            $('body').css('background-color', '#000000');
            $('h1, h2').css('color', '#000000');
            $('.darkmode').text('Light Mode');
        }
    });
});