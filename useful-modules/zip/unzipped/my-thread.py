from time import sleep
from threading import Thread

class MyThread(Thread):
  def __init__(self, text, time):
    self.text = text
    self.time = time

    super().__init__() # Thread.__init__(self)
  
  def run(self):
    sleep(self.time)
    print(self.text)

start = MyThread('Start', 0)
start.start()

first_thread = MyThread('First thread', 5)
first_thread.start()

second_thread = MyThread('Second thread', 10)
second_thread.start()

third_thread = MyThread('Third thread', 15)
third_thread.start()

fourth_thread = MyThread('Fourth thread', 20)
fourth_thread.start()

for i in range(20):
  print(i)
  sleep(1)
