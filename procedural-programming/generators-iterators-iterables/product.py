from itertools import product

people =  ['Luiz', 'Andre', 'Eduardo']

for group in product(people, repeat=2):
  print(group)
