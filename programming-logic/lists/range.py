my_list = list(range(0, 10))
print(my_list)

my_list.insert(1, 0.5)
my_list.insert(3, 1.5)
print(my_list)

my_list.remove(9)
my_list.remove(8)
print(my_list)

my_list.pop()
my_list.pop()
print(my_list)

sum = 0

for value in my_list:
  sum += value

print(sum)
