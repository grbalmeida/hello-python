from time import sleep
from threading import Thread

def my_thread(text, time):
  sleep(time)
  print(text)

thread = Thread(target=my_thread, args=('Hello world!', 10))
thread.start()
# thread.join() / block

while thread.is_alive():
  print('Waiting for thread')
  sleep(2)

print('Thread is over')
