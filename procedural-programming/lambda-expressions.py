def multiplication_without_lambda(first_number, second_number):
  return first_number * second_number

result = multiplication_without_lambda(2, 2)
print(result)

multiplication_with_lambda = lambda first_number, second_number: first_number * second_number
print(multiplication_with_lambda(2, 2))
