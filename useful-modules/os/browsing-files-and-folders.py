import os

file_path = input('Enter a path: ')
search_term = input('Enter a search term: ')

def formats_file_size(size):
  base = 1024
  kilobyte = base
  megabyte = base ** 2
  gigabyte = base ** 3
  terabyte = base ** 4
  petabyte = base ** 5

  if size < kilobyte:
    text = 'B'
  elif size < megabyte:
    size /= kilobyte
    text = 'K'
  elif size < gigabyte:
    size /= megabyte
    text = 'M'
  elif size < terabyte:
    size /= megabyte
    text = 'T'
  elif size < petabyte:
    size /= terabyte
    text = 'P'

  size = round(size, 2)

  return f'{size}{text}'

counter = 0

for root, directories, files in os.walk(file_path):
  for file in files:
    if search_term in file:
      try:
        counter += 1
        full_path = os.path.join(root, file)
        file_name, file_extension = os.path.splitext(full_path)
        file_size = os.path.getsize(full_path)

        print()
        print(f'I found the file: {file}')
        print(f'Full path: {full_path}')
        print(f'Filename: {file_name}')
        print(f'Extension: {file_extension}')
        print(f'Size in bytes: {file_size}')
        print(f'Formatted size: {formats_file_size(file_size)}')
      except PermissionError as error:
        print('No permisions')
      except FileNotFoundError as error:
        print('File not found')
      except Exception as error:
        print('Unknown error', error)

print()
print(f'{counter} files found')
