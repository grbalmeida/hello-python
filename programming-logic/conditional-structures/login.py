user = input('Username: ')
password = input('Password: ')

database_user = 'luiz'
database_password = '123456'

if database_user == user and database_password == password:
  print('You are logged in the system')
else:
  print('Username or password is invalid')

