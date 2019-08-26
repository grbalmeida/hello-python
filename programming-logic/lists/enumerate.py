my_string = 'Brazil is the soccer country'
my_list = my_string.split(' ')

for index, value in enumerate(my_list):
  print(f'{index} = {value} | {my_list[index]}')
