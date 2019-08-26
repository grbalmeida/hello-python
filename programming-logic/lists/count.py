my_string = 'Brazil is the soccer country. Brazil is a champion'

my_list = my_string.split(' ')

for value in my_list:
  print(f'The word {value} appeared {my_list.count(value)} times in the sentence')

word = ''
count = 0

for value in my_list:
  amount_of_times = my_list.count(value)

  if amount_of_times > count:
    count = amount_of_times
    word = value

print(f'The word that appeared most often is {word}. {count}x')
