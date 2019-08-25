name = 'Luiz Otavio'
age = 32
height = 1.80
is_greater_than_18 = age > 18
weight = 80
bmi = weight / height ** 2

print(name, 'is', age, 'years old and his BMI is', bmi, sep=' ')
print(f'{name} is {age} years old and his BMI is {bmi:.2f}')
print('{} is {} years old and his BMI is {:.2f}'.format(name, age, bmi))
print('{n} is {a} years old and his BMI is {b:.2f}'.format(n=name, a=age, b=bmi))

