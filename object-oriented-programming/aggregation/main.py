from shopping_cart import ShoppingCart
from product import Product

shopping_cart = ShoppingCart()

print(shopping_cart)
print(shopping_cart.products)

tshirt = Product('T-shirt', 50)
iPhone = Product('iPhone', 10000)
mug = Product('Mug', 15)

shopping_cart.list_products()

shopping_cart.insert_product(tshirt)
shopping_cart.insert_product(iPhone)
shopping_cart.insert_product(mug)

shopping_cart.list_products()

print(f'Total: {shopping_cart.total()}')
