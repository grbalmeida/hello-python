def hello_word():
  return 'Hello world!'

def master(function):
  return function()

running = master(hello_word)
print(running)

def another_master(function, *args, **kwargs):
  return function(*args, **kwargs)

def say_hi(name):
  return f'Hi {name}'

def greeting(name, greeting):
  return f'{greeting} {name}'

running = another_master(say_hi, 'Luiz')
print(running)

running = another_master(greeting, 'Luiz', greeting='Good morning')
print(running)
