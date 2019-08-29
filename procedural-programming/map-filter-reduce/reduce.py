from functools import reduce
from data import products, people, numbers

sum_of_numbers = reduce(lambda accumulator, item: accumulator + item, numbers, 0)
print(sum_of_numbers)

average_of_numbers = reduce(lambda accumulator, item: accumulator + item, numbers, 0) / len(numbers)
print(average_of_numbers)

sum_of_prices = reduce(lambda accumulator, item: accumulator + item['price'], products, 0)
print(sum_of_prices)

average_of_prices = reduce(lambda accumulator, item: accumulator + item['price'], products, 0) / len(products)
print(f'{average_of_prices:.2f}')

sum_of_ages = reduce(lambda accumulator, item: accumulator + item['age'], people, 0)
print(sum_of_ages)

average_of_ages = reduce(lambda accumulator, item: accumulator + item['age'], people, 0) / len(people)
print(f'{average_of_ages:.2f}')
