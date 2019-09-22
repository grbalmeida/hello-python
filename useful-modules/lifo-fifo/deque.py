from collections import deque

bank_queue = deque(maxlen=5)
bank_queue.append('John')
bank_queue.append('Maria')
bank_queue.append('Luiz')
bank_queue.append('Marcos')
bank_queue.append('Jose')
bank_queue.append('Ana')

print(bank_queue)

for name in bank_queue:
  print(name)

for i in range(5):
  print(f'{bank_queue.popleft()} left')
