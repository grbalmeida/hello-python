"""
  Arithmetic operators

  +  -> Sum
  -  -> Subtraction
  *  -> Multiplication
  /  -> Division
  // -> Whole division
  ** -> Exponentiation
  %  -> Mod = Rest of division
"""

print('Multiplication:', 10 * 10)
print('Sum:', 10 + 10)
print('Subtraction:', 10 - 5)
print('Division:', 10 / 2)
print('Whole division:', 10 // 3)
print('Whole division:', 10.5 // 3)
print('Exponentiation:', 2 ** 10)
print('Mod:', 10 % 2)
print('Mod:', 10 % 3)

# Parentheses alternate order of precedence

print((5 + 2) * 10)
print((5 * 3) + 10 + (10 / 2))

print('Concatenation:', '5' + '5')
print('Repetition:', 5 * 'a')

print('Luiz' + ' ' + 'Otavio' + ' ' + 'is' + ' ' + str(32) + ' ' + 'years' + ' ' + 'old')
print('Luiz', 'Otavio', 'is', str(32), 'years', 'old', sep=' ')
print('Luiz' + ' ' + 'Otavio')
print('Luiz', 'Otavio', sep=' ')

