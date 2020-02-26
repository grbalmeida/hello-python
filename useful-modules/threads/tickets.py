from time import sleep
from threading import Thread, Lock

class Tickets:
  def __init__(self, stock):
    self.stock = stock
    self.lock = Lock()

  def buy(self, quantity):
    self.lock.acquire()

    if self.stock < quantity:
      print("We don't have enough tickets")
      self.lock.release()
      return

    sleep(1)
   
    self.stock -= quantity
    print(f'You have bought {quantity} tickets. We still have {self.stock}')
    self.lock.release()

if __name__ == '__main__':
  tickets = Tickets(10)
  threads = []

  for i in range(1, 20):
    thread = Thread(target=tickets.buy, args=(i,))
    threads.append(thread)

  for thread in threads:
    thread.start()

  running = True

  while running:
    running = False

    for thread in threads:
      if thread.is_alive():
        running = True

  print(f'Tickets: {tickets.stock}')
