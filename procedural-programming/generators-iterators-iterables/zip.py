from itertools import count

index = count()
cities = ['Sao Paulo', 'Belo Horizonte', 'Salvador', 'Monte Belo']
states = ['SP', 'MG', 'BA']

cities_states = zip(
  index,
  cities,
  states
)

for index, city, state in cities_states:
  print(f'{index} = {city} - {state}')
