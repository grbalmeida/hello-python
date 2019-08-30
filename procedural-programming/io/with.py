from FILE import FILE

with open(FILE, 'w+') as file:
  file.write('First line\n')
  file.write('Second line\n')
  file.write('Third line')

  file.seek(0, 0)

  print(file.read())
