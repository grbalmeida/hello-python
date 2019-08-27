first_tuple = (1, 2, 3, 'Luiz Otavio')
second_tuple = 1, 2, 3, 'Luiz Otavio'
third_tuple = first_tuple + second_tuple

print(first_tuple)
print(type(first_tuple))

for value in first_tuple:
  print(value)

for value in second_tuple:
  print(value)

for value in third_tuple:
  print(value)

print(first_tuple[:1])
print(first_tuple[::])
print(second_tuple[3:])
print(second_tuple[2:])
print(third_tuple[7:])
