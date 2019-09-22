import random

integer = random.randint(10, 20)
print(integer)

floating_point = random.uniform(10, 20)
print(floating_point)

between_zero_and_one = random.random()
print(between_zero_and_one)

randrange = random.randrange(900, 1000, 10)
print(randrange)

people = ['Luiz', 'Otavio', 'Maria', 'Rose', 'Jenny', 'Danilo', 'Felipe']

chosen_person = random.choice(people)
print(chosen_person)

chosen_people = random.choices(people, k=2)
print(chosen_people)

two_unique_people = random.sample(people, 2)
print(two_unique_people)

single_person = random.choice(people)
print(single_person)

random.shuffle(people)
print(people)
