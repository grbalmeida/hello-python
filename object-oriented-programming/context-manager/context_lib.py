from contextlib import contextmanager

@contextmanager
def open_file(filename, mode):
  try:
    file = open(filename, mode)
    print('Opening file')
    yield file
  finally:
    print('Closing file')
    file.close()

with open_file('object-oriented-programming/context-manager/my_file.txt', 'w') as file:
  file.write('First line\n')
  file.write('Second line\n')
  file.write('Third line')
