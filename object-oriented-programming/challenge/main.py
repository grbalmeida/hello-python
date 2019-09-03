from random import randint
from bank import Bank
from checking_account import CheckingAccount
from savings_account import SavingsAccount
from customer import Customer

bank = Bank()

luiz = Customer('Luiz', 25)
maria = Customer('Maria', 52)

savings_account = SavingsAccount(1111, 32460, 0)
checking_account = CheckingAccount(2222, 32461, 0)

luiz.insert_account_number(savings_account)
maria.insert_account_number(checking_account)

bank.insert_account(savings_account)
bank.insert_customer(luiz)

bank.insert_account(checking_account)
bank.insert_customer(maria)

for customer in [luiz, maria]:
  if bank.authenticate(customer):
    customer.account.deposit(randint(500, 1000))
    customer.account.withdraw(randint(50, 100))
  else:
    print('Unauthenticated customer')
