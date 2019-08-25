time = input('Enter a time (0-23): ')

if time.isdigit():
  time = int(time)

  if time < 0 or time > 23:
    print('Time must be between 0 and 23')
  else:
    if time <= 11:
      print('Good morning')
    elif time <= 17:
      print('Good afternoon')
    else:
      print('Good night')
else:
  print('Please enter a time between 0 and 23')

