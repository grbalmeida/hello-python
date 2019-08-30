from person import Person

first_person = Person(name='Luiz', age=29, is_eating=True, is_speaking=False)
second_person = Person(name='Joao', age=32, is_eating=False, is_speaking=True)

print(first_person)
print(second_person)

first_person.eat('Apple')
first_person.speak('Hi')
first_person.stop_eating()
first_person.stop_eating()
first_person.speak('Hi')
first_person.stop_talking()
first_person.stop_talking()
first_person.speak('Hi')
first_person = None

second_person.eat('Potato')
second_person.speak('Hello')
second_person.stop_eating()
second_person.stop_eating()
second_person.speak('Hello')
second_person.stop_talking()
second_person.stop_talking()
second_person.speak('Hello')
second_person = None
