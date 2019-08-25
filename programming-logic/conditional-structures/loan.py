name = input('What is your name? ')
age = int(input('What is your age? '))

minimum_age = 20
max_age = 30

if age >= minimum_age and age <= max_age:
  print(f'{name} can get the loan')
else:
  print(f"{name} can't take the loan")

