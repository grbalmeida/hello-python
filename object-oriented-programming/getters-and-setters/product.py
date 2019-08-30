class Product:
  def __init__(self, name, price):
    self.name = name
    self.price = price

  def discount(self, percentage):
    self.price = self.price - (self.price * (percentage / 100))

  @property
  def price(self):
    return self._price

  @price.setter
  def price(self, value):
    if isinstance(value, str):
      value = float(value.replace('R$', ''))

    self._price = value

  @property
  def name(self):
    return self._name
  
  @name.setter
  def name(self, value):
    self._name = value.title()

tshirt = Product('t-shirt', 50)
tshirt.discount(10)
print(tshirt.name)
print(tshirt.price)

mug = Product('mug', 'R$15')
mug.discount(10)
print(mug.name)
print(mug.price)
