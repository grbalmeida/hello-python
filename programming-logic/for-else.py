my_list = ['Luiz Otavio', 'John', 'Maria']

for value in my_list:
  if value.lower().startswith('j'):
    break
else:
  print('There is no word starting with J')
