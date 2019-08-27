first_set = {1, 2, 3, 4, 10}
second_set = {4, 5, 6, 7, 8}

third_set = first_set ^ second_set
print(third_set)

third_set = first_set.symmetric_difference(second_set)
print(third_set)
