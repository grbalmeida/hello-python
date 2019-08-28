from itertools import combinations

people = ['Luiz', 'Andre', 'Eduardo', 'Leticia', 'Fabricio', 'Rose']

for group in combinations(people, 2):
  print(group)
