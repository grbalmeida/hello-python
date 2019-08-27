my_dictionary = {}

my_dictionary['first_key'] = 'First value'
my_dictionary['second_key'] = 'Second value'
my_dictionary['third_key'] = 'Third value'

for value in my_dictionary.values():
  print(value)

for key in my_dictionary.keys():
  print(key)

for item in my_dictionary.items():
  print(item)

for key, value in my_dictionary.items():
  print(f'key = {key} | value = {value}')
