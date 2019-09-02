from account import Account

class CheckingAccount(Account):
  def __init__(self, agency, account_number, balance, limit=100):
    super().__init__(agency, account_number, balance)
    self._limit = limit

  @property
  def limit(self):
    return self._limit

  def withdraw(self, value):
    if (self.balance + self.limit) < value:
      print('Insufficient funds')
      return

    self._balance -= value
    self.details()
