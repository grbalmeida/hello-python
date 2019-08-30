from FILE import FILE

file = open(FILE, 'r')

for index, line in enumerate(file):
  print(f'{index + 1} {line}', end='')

file.close()
