names = ['Luiz', 'John', 'Maria', 'Jorge', 'Luisa']

first_name, second_name, third_name, *other_names, last_of_the_list = names

print(first_name)
print(second_name)
print(third_name)
print(other_names)
print(last_of_the_list)

other_list = [1, 2, 3, 4, 5]
*top_of_list, penultimate, last = other_list

print(top_of_list)
print(penultimate)
print(last)
