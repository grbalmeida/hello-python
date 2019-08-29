def division(first_number, second_number):
  if second_number == 0:
    raise ValueError('The <second_number> parameter cannot be zero')

  return first_number / second_number

try:
  print(division(2, 0))
except ValueError as error:
  print(error)
