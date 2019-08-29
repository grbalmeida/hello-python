try:
  my_list = []
  print(my_list[0])
except IndexError as error:
  print(error.args)
  print(f'You attempted to access an index out of range: {error}')
else:
  print('The code was executed without throwing any exceptions')
