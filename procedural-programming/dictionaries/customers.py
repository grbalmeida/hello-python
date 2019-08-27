customers = {
  'customer_1': {
    'name': 'Luiz',
    'lastname': 'Otavio'
  },
  'customer_2': {
    'name': 'Joao',
    'lastname': 'Moreira'
  },
  'customer_3': {
    'name': 'Maria',
    'lastname': 'Moreira'
  }
}

for customer_key, customer_value in customers.items():
  print(f'Showing {customer_key}')

  for data_key, data_value in customer_value.items():
    print(f'\t{data_key} = {data_value}')
