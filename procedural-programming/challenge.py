def greeting(greeting, name):
  return f'{greeting} {name}'

print(greeting('Hello', 'Maria')) # Hello Maria

def sum_three_numbers(first_number=0, second_number=0, third_number=0):
  return first_number + second_number + third_number

print(sum_three_numbers(10, 20, 30)) # 60

def percentage_increase(value, increase):
  return value + (value / 100 * increase)

print(percentage_increase(380, 10)) # 418

def fizz_buzz(number):
  if number % 5 == 0 and number % 3 == 0:
    return 'FizzBuzz'
  elif number % 3 == 0:
    return 'Fizz'
  elif number % 5 == 0:
    return 'Buzz'
  else:
    return number

print(fizz_buzz(15)) # FizzBuzz
print(fizz_buzz(9))  # Fizz
print(fizz_buzz(10)) # Buzz
print(fizz_buzz(11)) # 11
