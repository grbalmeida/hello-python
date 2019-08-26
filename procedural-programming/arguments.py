def my_function(*args, **kwargs):
  print(args)
  print(kwargs)
  print(kwargs.get('city'))   # San Francisco
  print(kwargs.get('number')) # 30
  print(kwargs.get('name'))   # None

my_function(10, 20, number=30, city='San Francisco')
