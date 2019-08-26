while True:
  print()
  first_number = input('Enter a number: ')
  second_number = input('Enter another number: ')
  operator = input('Enter an operator: ')

  if not first_number.isnumeric() or not second_number.isnumeric():
    print('You need to enter a number')
    continue

  first_number = int(first_number)
  second_number = int(second_number)

  if operator == '+':
    print(first_number + second_number)
  elif operator == '-':
    print(first_number - second_number)
  elif operator == '/':
    print(first_number / second_number)
  elif operator == '*':
    print(first_number * second_number)
  else:
    print('Invalid operator')

