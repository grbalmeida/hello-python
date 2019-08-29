from sales.price import decrease, increase
from sales.formatting.real import real

if __name__ == '__main__':
  price = 49.90
  price_with_decrease = decrease(value=price, percentage=23, formats=True)
  price_with_increase = increase(value=price, percentage=15)

  print(price_with_decrease)
  print(real(price_with_increase))
