string = '012345678901234567890123456789012345678901234567890123456789'

quantity = 10
my_list = [string[index:index + quantity] for index in range(0, len(string), quantity)]
concatenate_with_dot = '.'.join(my_list)

print(my_list)
print(concatenate_with_dot)
