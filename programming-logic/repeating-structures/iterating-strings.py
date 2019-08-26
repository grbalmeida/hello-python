my_string = 'The mouse that gnawed the oak-tree'
new_string = ''
string_length = len(my_string)
counter = 0

while counter < string_length:
  if my_string[counter] == 'r':
    new_string += my_string[counter].upper()
  else:
    new_string += my_string[counter]

  print(my_string[counter])
  counter += 1

print(new_string)

