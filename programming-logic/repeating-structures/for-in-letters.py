text = 'Python'
new_string = ''

for letter in text:
  if letter == 'P':
    new_string += letter.lower()
  elif letter == 'h':
    new_string += letter.upper()
  else:
    new_string += letter

print(new_string)

