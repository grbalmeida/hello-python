products = [
  ['Rice', 8],
  ['Bean', 5],
  ['Spaghetti', 3.6],
  ['Garlic', 1.8],
  ['Potatoes', 2.3]
]

print(sorted(products, key=lambda item: item[0]))
print(sorted(products, key=lambda item: item[0], reverse=True))
print(sorted(products, key=lambda item: item[1]))
print(sorted(products, key=lambda item: item[1], reverse=True))
print(products)
