def customers_list(customers_iterable, internal_list=None):
  if internal_list is None:
    internal_list = []

  internal_list.extend(customers_iterable)
  
  return internal_list

customers = customers_list(['Joao', 'Maria', 'Eduardo'])
print(customers)

customers = customers_list(['Marcos', 'Jonas', 'Zico'])
print(customers)

customers = customers_list(['Jose'])
print(customers)
