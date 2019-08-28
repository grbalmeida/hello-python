from itertools import permutations

people = ['Luiz', 'Andre', 'Eduardo']

for group in permutations(people, 2):
  print(group)
