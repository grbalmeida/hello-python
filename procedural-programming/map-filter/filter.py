from data import numbers, people, products

numbers_greater_than_5 = list(filter(lambda number: number > 5, numbers))
print(numbers_greater_than_5)

numbers_less_than_5 = list(filter(lambda number: number < 5, numbers))
print(numbers_less_than_5)

prices_greater_than_10 = list(filter(lambda product: product['price'] > 10, products))
print(prices_greater_than_10)

prices_greater_than_5 = list(filter(lambda product: product['price'] > 5, products))
print(prices_greater_than_5)

prices_less_than_5 = list(filter(lambda product: product['price'] < 5, products))
print(prices_less_than_5)

people_over_30 = list(filter(lambda person: person['age'] > 30, people))
print(people_over_30)

people_under_30 = list(filter(lambda person: person['age'] < 30, people))
print(people_under_30)
