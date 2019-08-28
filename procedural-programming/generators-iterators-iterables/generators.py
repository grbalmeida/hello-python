import sys
import time

def generates():
  for number in range(100):
    yield number
    time.sleep(0.1)

generator = generates()

print(generator)
print(hasattr(generator, '__next__'))
print(hasattr(generator, '__iter__'))

for value in generator:
  print(value)
