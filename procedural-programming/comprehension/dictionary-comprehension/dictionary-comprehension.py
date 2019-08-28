my_list = [
  ('first_key', 'First value'),
  ('second_key', 'Second value')
]

my_dictionary = {key.upper(): value.upper() for key, value in my_list}

print(my_dictionary)
