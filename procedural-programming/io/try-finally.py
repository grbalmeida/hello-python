from FILE import FILE

try:
  file = open(FILE, 'r')
  print(file.read())
except FileNotFoundError as error:
  print(f'Unable to read file: {error.filename}')
finally:
  print('Closing the file: {error.filename}')
