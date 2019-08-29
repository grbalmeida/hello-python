try:
  my_tuple = (1, 2, 3)
  my_tuple[3] = 4
except TypeError as error:
  print(error.args)
  print(f'Tuple doest not support item assignment: {error}')
else:
  print('The code was executed without throwing any exceptions')
