my_list = list(range(0, 10))

my_tuple = [
  (first_value, second_value)
  for first_value in my_list
  for second_value in range(3)
]

print(my_tuple)
