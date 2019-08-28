from types import GeneratorType

variable = zip('Hello', 'Hi')
print(isinstance(variable, GeneratorType))

variable = ((x, y) for x, y in zip('Hello', 'Hi'))
print(isinstance(variable, GeneratorType))
