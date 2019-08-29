from functools import reduce

def multiply(numbers):
  return reduce(lambda accumulator, item: accumulator * item, numbers, 1)
