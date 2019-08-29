def division(first_number, second_number):
  try:
    return first_number / second_number
  except ZeroDivisionError as error:
    print('A mathematical error has ocurred')
    print(f'You can\'t divide a number by zero: {error}')
    print(error.args)
    raise

try:
  print(division(2, 0))
except:
  print('An error has ocurred')
