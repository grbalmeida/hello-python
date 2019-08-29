try:
  print(nonexistent_variable)
except NameError as error:
  print(error.args)
  print(f'The variable was not set: {error}')
else:
  print('The code was executed without throwing any exceptions')
