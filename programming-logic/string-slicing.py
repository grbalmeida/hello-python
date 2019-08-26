text = 'Python'

print(text[0]) # P
print(text[1]) # y
print(text[2]) # t
print(text[3]) # h
print(text[4]) # o
print(text[5]) # n

print(text[-1]) # n
print(text[-2]) # o
print(text[-3]) # h
print(text[-4]) # t
print(text[-5]) # y
print(text[-6]) # P

new_string = text[0:2] # Py
print(new_string)

new_string = text[:2] # Py
print(new_string)

new_string = text[2:6] # thon
print(new_string)

new_string = text[2:] # thon
print(new_string)

new_string = text[0:6] # Python
print(new_string)

new_string = text[:6] # Python
print(new_string)

new_string = text[0::2] # Pto
print(new_string)

new_string = text[0::3] # Ph
print(new_string)

new_string = text[0::4] # Po
print(new_string)

new_string = text[0::5] # Pn
print(new_string)

new_string = text[::5] # Pn
print(new_string)

