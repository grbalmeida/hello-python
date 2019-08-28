my_list = [1, 2, 3, 4, 5]
print(hasattr(my_list, '__next__'))

my_list = iter(my_list)
print(hasattr(my_list, '__next__'))

print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
print(next(my_list))
