from FILE import FILE

with open(FILE, 'a+') as file:
  file.write('\nFourth line')
  file.seek(0, 0)
  print(file.read())
