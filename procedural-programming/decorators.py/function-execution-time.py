from time import time, sleep

def function_execution_time(function):
  def internal(*args, **kwargs):
    start_time = time()
    result = function(*args, **kwargs)
    end_time = time()
    difference = (end_time - start_time) * 1000
    print(f'The {function.__name__} function took {difference:.2f}/ms to execute')
    return result
  
  return internal

@function_execution_time
def time_consuming_function():
  for index in range(5):
    print(index)
    sleep(0.5)

time_consuming_function()
