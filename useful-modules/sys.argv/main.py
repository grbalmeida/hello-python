#!/usr/bin/env python3

import sys
import os

argv = sys.argv
number_of_arguments = len(argv)

if number_of_arguments <= 1:
  print('Missing arguments')
  print('-f', 'To list all files in this folder', sep='\t')
  print('-d', 'To list all directories in this folder', sep='\t')
  sys.exit()

only_files = '-f' in argv
only_directories = '-d' in argv

for file in os.listdir('.'):
  if only_files:
    if os.path.isfile(file):
      print(file)

  if only_directories:
    if os.path.isdir(file):
      print(file)
