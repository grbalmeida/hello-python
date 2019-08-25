name = input('Enter your name: ')
name_length = len(name)

if name_length <= 4:
  print('Your name is short')
elif name_length <= 6:
  print('Your name is normal')
else:
  print('Your name is too big')

