from time import sleep
from collections import deque

queue = deque(maxlen=10)

for i in range(100):
  queue.append(i)
  sleep(.5)
  print(queue)
