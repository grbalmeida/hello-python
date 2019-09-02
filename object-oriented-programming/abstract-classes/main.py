from savings_account import SavingsAccount
from checking_account import CheckingAccount

savings_account = SavingsAccount(1111, 2222, 0)
savings_account.deposit(100)
savings_account.deposit(150)
savings_account.deposit(280)

savings_account.withdraw(10)
savings_account.withdraw(15)
savings_account.withdraw(1000)

checking_account = CheckingAccount(agency=1111, account_number=3333, balance=0, limit=500)

checking_account.deposit(100)
checking_account.withdraw(250)
checking_account.withdraw(260)
checking_account.withdraw(500)
