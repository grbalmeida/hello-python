from account import Account

class SavingsAccount(Account):
  def withdraw(self, value):
    if self.balance < value:
      print('Insufficient funds')
      return

    self._balance -= value
    self.details()
