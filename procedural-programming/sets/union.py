first_set = {1, 2, 3}
second_set = {3, 4, 5}

third_set = first_set | second_set
print(third_set)

third_set = third_set.union({6, 8, 9})
print(third_set)
