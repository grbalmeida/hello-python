first_list = [1, 2, 3]
second_list = [4, 5, 6]
third_list = first_list + second_list

print(first_list)
print(second_list)
print(third_list)

third_list = []
third_list.extend(first_list)
third_list.extend(second_list)
print(third_list)
