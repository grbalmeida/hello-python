from functools import reduce

class ShoppingCart:
  def __init__(self):
    self.products = []

  def insert_product(self, product):
    self.products.append(product)

  def list_products(self):
    for product in self.products:
      print(product.name, product.price)

  def total(self):
    my_total = reduce(lambda accumulator, item: accumulator + item.price, self.products, 0)
    return my_total
