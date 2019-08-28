cart = []

cart.append(('First product', 30))
cart.append(('Second product', 20))
cart.append(('Third product', 50))

total = sum([price for product, price in cart])

print(total)
