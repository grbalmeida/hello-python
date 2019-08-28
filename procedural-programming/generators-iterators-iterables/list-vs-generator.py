import sys

my_list = [number for number in range(10000)]
my_generator = (number for number in range(10000))

print(type(my_list))
print(type(my_generator))

print(sys.getsizeof(my_list))       # 87624
print(sys.getsizeof(my_generator))  # 120
