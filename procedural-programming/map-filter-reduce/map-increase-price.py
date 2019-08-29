from data import products

def increase_price(product):
  product['price'] = round(product['price'] * 1.05, 2)
  return product

new_products = map(increase_price, products)

for product in new_products:
  print(product)
