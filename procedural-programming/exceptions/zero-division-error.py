try:
  print(10 / 0)
except ZeroDivisionError as error:
  print(error.args)
  print(f'You tried to divide a number by zero: {error}')
else:
  print('The code was executed without throwing any exceptions')
