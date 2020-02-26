from time import sleep
from threading import Thread

def my_thread(text, time):
  sleep(time)
  print(text)

first_thread = Thread(target=my_thread, args=('First thread!', 5))
first_thread.start()

second_thread = Thread(target=my_thread, args=('Second thread!', 1))
second_thread.start()

third_thread = Thread(target=my_thread, args=('Third thread!', 2))
third_thread.start()

for i in range(20):
  print(i)
  sleep(.5)
