def first_function(message):
  print(message)

def second_function():
  return first_function

print(id(first_function), id(second_function()))
print(id(first_function) == id(second_function())) # True
