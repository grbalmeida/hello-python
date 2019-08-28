import sys
import time

def generates():
  variable = 'First value'
  yield variable
  variable = 'Second value'
  yield variable
  variable = 'Third value'
  yield variable

generator = generates()

for value in generator:
  print(value)
