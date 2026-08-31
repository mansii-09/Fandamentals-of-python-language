def update_cart(cart,item,qty):
    cart[item] = qty
    return cart

cart= {
    "Shirt" : 2,
    "Shoes" : 1
}

cart = update_cart(cart,"Jeans", 3)
print(cart)

cart = update_cart(cart,"Shirt",5)
print(cart)
