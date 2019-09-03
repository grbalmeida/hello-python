from account import Account

class CheckingAccount(Account):
  def __init__(self, agency, account, balance, limit=100):
    super().__init__(agency, account, balance)
    self.limit = limit

  def withdraw(self, value):
    if self.balance + self.limit < value:
      print('Insufficient funds')
      return

    self.balance -= value
    self.details()
