name = 'Luiz'
age = 32
height = 1.80
weight = 80.5
bmi = weight / height ** 2
current_year = 2019
year_of_birth = current_year - age

print(f'{name} is {age} years old, {height:.2f} tall and weight {weight:.2f} kilograms')
print(f'{name} BMI is {bmi:.2f}')
print(f'{name} was born in {year_of_birth}')

