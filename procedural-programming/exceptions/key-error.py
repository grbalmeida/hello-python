try:
  my_dict = {}
  print(my_dict['name'])
except KeyError as error:
  print(error.args)
  print(f'You attempted to access a dictionary key that does not exist: {error}')
else:
  print('The code was executed without throwing any exceptions')