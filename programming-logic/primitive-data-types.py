"""
  "Primitive" data types
  str - string
  int - integer
  float - floating point number
  bool - boolean
"""

# str

print('This is a string')
print("This is a string")
print(type('This is a string'))
print(type("This is a string"))

# int

print(10)
print(-10)
print(type(10))
print(type(-10))

# float

print(1.5)
print(-1.5)
print(type(1.5))
print(type(-1.5))

# bool

print(True)
print(False)
print(10 == 10)
print('l' == 'L')
print(type(True))
print(type(False))
print(type(10 == 10))
print(type('l' == 'L'))

# Cast

print('Luiz', type('Luiz'), bool('Luiz'))
print('10', type('10'), int('10'), type(int('10')))
print('10.0', type('10.0'), float('10.0'), type(float('10.0')))
print(10, type(10), str(10), type(str(10)))

# Falsy values

print(bool(''))      # False
print(bool(0))       # False
print(bool(0.0))     # False
print(bool(None))    # False
print(bool(False))   # False
print(bool([]))      # False
print(bool({}))      # False
print(bool(()))      # False
print(bool(b''))     # False
print(bool(set()))   # False

print('Gilvan', type('Gilvan'))
print(22, type(22))
print(1.87, type(1.87))
print(22 > 18, type(22 > 18))

