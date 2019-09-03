class Bank:
  def __init__(self):
    self.agencies = [1111, 2222, 3333]
    self.customers = []
    self.accounts = []
  
  def insert_customer(self, customer):
    self.customers.append(customer)

  def insert_account(self, account):
    self.accounts.append(account)

  def authenticate(self, customer):
    if customer not in self.customers:
      return

    if customer.account not in self.accounts:
      return

    if customer.account.agency not in self.agencies:
      return

    return True
