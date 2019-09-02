from customer import Customer
from student import Student
from person import Person

luiz = Customer('Luiz', 45)
maria = Student('Maria', 54)
john = Person('John', 43)

print(luiz.name)
print(luiz.class_name)
luiz.speek()

print(maria.name)
print(maria.class_name)
maria.speek()

print(john.name)
john.speek()
