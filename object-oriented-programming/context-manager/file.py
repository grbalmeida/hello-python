class File:
  def __init__(self, file, mode):
    print('INIT')
    self.file = open(file, mode)

  def __enter__(self):
    print('Joined the class')
    return self.file

  def __exit__(self, exc_type, exc_value, exc_tb):
    print('Left class')
    self.file.close()
    return True

with File('object-oriented-programming/context-manager/my_file.txt', 'w') as file:
  file.write('Something')
