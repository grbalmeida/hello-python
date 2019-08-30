import json

people = [
  {'name': 'Luiz', 'age': 25},
  {'name': 'Rose', 'age': 30}
]

json_file = json.dumps(people, indent=True)
print(json_file)

with open('procedural-programming/io/people.json', 'w+') as file:
  file.write(json_file)
  file.seek(0, 0)
  print(file.read())
