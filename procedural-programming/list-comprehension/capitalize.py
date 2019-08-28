names = ['luiz', 'MaUrO', 'MARIA']

names_with_first_capital_letter = [
  f'{name[0].upper()}{name[1:].lower()}'
  for name in names
]

print(names)
print(names_with_first_capital_letter)
