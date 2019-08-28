from data import people

names = map(lambda person: person['name'], people)
print(list(names))

ages = map(lambda person: person['age'], people)
print(list(ages))
