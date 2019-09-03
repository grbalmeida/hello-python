from person import Person

class Customer(Person):
  def __init__(self, name, age):
    super().__init__(name, age)
    self.account = None

  def insert_account_number(self, account):
    self.account = account
