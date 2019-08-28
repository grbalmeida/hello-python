from data import products

prices = list(map(lambda product: product['price'], products))

print(prices)
