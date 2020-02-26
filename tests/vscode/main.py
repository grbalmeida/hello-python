from calculator import sum

print(sum(10, 20))
print(sum(-10, 20))
print(sum(10.5, 20.5))
print(sum(1.5, 2.5))

try:
    print(sum('15', 15))
except AssertionError as e:
    print(e)

try:
    print(sum(15, '15'))
except AssertionError as e:
    print(e)