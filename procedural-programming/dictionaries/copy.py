my_dictionary = {
  'first_key': 'First value',
  'second_key': 'Second value',
  'third_key': 'Third value'
}

first_copy = my_dictionary
print(first_copy == my_dictionary)
print(id(first_copy) == id(my_dictionary))  # True
print(id(first_copy), id(my_dictionary))

second_copy = my_dictionary.copy()
print(second_copy)
print(second_copy == my_dictionary)
print(id(second_copy) == id(my_dictionary)) # False
print(id(second_copy), id(my_dictionary))
