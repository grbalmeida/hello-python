from customer import Customer

luiz = Customer('Luiz', 32)
luiz.insert_address('Belo Horizonte', 'MG')
print(luiz.name)
luiz.list_addresses()
del luiz

maria = Customer('Maria', 55)
maria.insert_address('Salvador', 'BA')
maria.insert_address('Rio de Janeiro', 'RJ')
print(maria.name)
maria.list_addresses()
del maria

john = Customer('John', 19)
john.insert_address('Sao Paulo', 'SP')
print(john.name)
john.list_addresses()
del john
