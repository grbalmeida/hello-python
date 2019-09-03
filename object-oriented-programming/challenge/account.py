from abc import ABC, abstractmethod

class Account(ABC):
  def __init__(self, agency, account, balance):
    self.agency = agency
    self.account = account
    self.balance = balance

  def deposit(self, value):
    self.balance += value
    self.details()

  def details(self):
    print(f'Agency: {self.agency}')
    print(f'Account: {self.account}')
    print(f'Balance: {self.balance}')
    print('#' * 50)

  @abstractmethod
  def withdraw(self, value):
    pass
