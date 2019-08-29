try:
  from nonexistent_module import nonexistent_function
except ModuleNotFoundError as error:
  print(error)
else:
  print('The code was executed without throwing any exceptions')
