import json

def print_person(person):
  name = person.get('name')
  age = person.get('age')
  print(f'Name: {name} - Age: {age}')

with open('procedural-programming/io/people.json', 'r') as file:
  json_file = file.read()
  people = json.loads(json_file)
  for person in people:
    print_person(person)
