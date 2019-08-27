products = [
  ['Rice', 8],
  ['Bean', 5],
  ['Spaghetti', 3.6],
  ['Garlic', 1.8],
  ['Potatoes', 2.3]
]

def sort_without_lambda(item):
  return item[1]

products.sort(key=sort_without_lambda, reverse=True)
print(products)

products.sort(key=lambda item: item[1])
print(products)

products.sort(key=lambda item: item[0])
print(products)

products.sort(key=lambda item: item[0], reverse=True)
print(products)
