from FILE import FILE

file = open(FILE, 'r')
lines = file.readlines()

for index, line in enumerate(lines):
  print(f'{index + 1} {line}', end='')

file.close()
