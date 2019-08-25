first_number = 10
second_number = 3
division = first_number / second_number

print('{:.2f}'.format(division))
print(f'{division:.2f}')

name = 'Luiz Otavio'
print(f'{name:s}')

first_number = 1
print(f'{first_number:0>10}')
print(f'{first_number:0<10}')
print(f'{first_number:0^10}')

second_number = 1150
print(f'{second_number:0>10}')
print(f'{second_number:0<10}')
print(f'{second_number:0^10}')

print(f'{second_number:0>10.2f}')
print(f'{second_number:0<10.2f}')
print(f'{second_number:0^10.2f}')

name = 'Otavio Miranda'
print(f'{name:#^50}')
print(f'{name:#>50}')
print(f'{name:#<50}')

formatted_name = '{}'.format(name)
print(formatted_name)

formatted_name = '{:@>50}'.format(name)
print(formatted_name)

formatted_name = '{:@<50}'.format(name)
print(formatted_name)

formatted_name = '{n:0<20}'.format(n=name)
print(formatted_name)

