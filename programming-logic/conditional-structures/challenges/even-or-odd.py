integer = input('Enter a integer: ')

if integer.isdigit():
  integer = int(integer)

  if integer % 2 == 0:
    print(f'{integer} is even')
  else:
    print(f'{integer} is odd')
else:
  print('This is not an integer')

