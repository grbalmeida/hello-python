import os
import shutil
import sys

argv = sys.argv
original_path = '.'
new_path = f'{original_path}/new-path'
js = f'{original_path}/js'

def mkdir():
  try:
    os.mkdir(new_path)
  except FileExistsError as error:
    print(f'Folder {new_path} already exists')

def mv():
  for root, directories, files in os.walk(original_path):
    for file in files:
      old_file_path = os.path.join(root, file)
      new_file_path = os.path.join(new_path, file)

      shutil.move(old_file_path, new_file_path)
      print(f'File {file} moved successfully')

def cp():
  for root, directories, files in os.walk(original_path):
    for file in files:
      old_file_path = os.path.join(root, file)
      new_file_path = os.path.join(js, file)

      if '.js' in file:
        shutil.copy(old_file_path, new_file_path)
        print('Successfully copied javascript files')

def rm():
  for root, directories, files in os.walk(new_path):
    for file in files:
      old_file_path = os.path.join(root, file)
      new_file_path = os.path.join(new_path, file)

      os.remove(new_file_path)
      print(f'{file} file deleted successfully')

if '-mkdir' in argv:
  mkdir()

if '-mv' in argv:
  mv()

if '-cp' in argv:
  cp()

if '-rm' in argv:
  rm()
