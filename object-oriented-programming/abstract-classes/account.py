from abc import ABC, abstractmethod

class Account(ABC):
  def __init__(self, agency, account_number, balance):
    self._agency = agency
    self._account_number = account_number
    self._balance = balance

  @property
  def agency(self):
    return self._agency
  
  @property
  def account_number(self):
    return self._account_number

  @property
  def balance(self):
    return self._balance

  @balance.setter
  def balance(self, value):
    if not isinstance(value, (int, float)):
      raise ValueError('Balance must be numeric')
    
    self._balance = value

  def deposit(self, value):
    if not isinstance(value, (int, float)):
      raise ValueError('Deposit amount must be numeric')

    self._balance += value
    self.details()

  def details(self):
    print(f'Agency: {self.agency}')
    print(f'Account number: {self.account_number}')
    print(f'Balance: {self.balance}')
    print('#' * 50)

  @abstractmethod
  def withdraw(self, value):
    pass
