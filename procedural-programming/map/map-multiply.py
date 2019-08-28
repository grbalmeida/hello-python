from data import numbers

multiply_by_2 = list(map(lambda number: number * 2, numbers))
print(multiply_by_2)
multiply_by_2 = [number * 2 for number in numbers]
print(multiply_by_2)

multiply_by_3 = list(map(lambda number: number * 3, numbers))
print(multiply_by_3)
multiply_by_3 = [number * 3 for number in numbers]
print(multiply_by_3)
