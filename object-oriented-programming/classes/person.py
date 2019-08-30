from datetime import datetime

class Person:
  current_year = int(datetime.strftime(datetime.now(), '%Y'))

  def __init__(self, name, age, is_eating=False, is_speaking=False):
    self.name = name
    self.age = age
    self.is_eating = is_eating
    self.is_speaking = is_speaking

  def __del__(self):
    print('#' * 30)

  def __str__(self):
    return (
      f'{"#" * 30}'
      f'\nName: {self.name}\n'
      f'Age: {self.age}\n'
      f'Is eating? {self.is_eating}\n'
      f'Is speaking? {self.is_speaking}\n'
    )

  def speak(self, subject_matter):
    if self.is_eating:
      print(f'{self.name} can\'t talk while eating')
      return
    
    if self.is_speaking:
      print(f'{self.name} is already talking')
      return

    print(f'{self.name} is talking: {subject_matter}')
    self.is_speaking = True

  def stop_talking(self):
    if not self.is_speaking:
      print(f'{self.name} is not talking')
      return
    
    print(f'{self.name} stopped talking')
    self.is_speaking = False

  def eat(self, food):
    if self.is_speaking:
      print(f'{self.name} can\'t eat while talking')
      return

    if self.is_eating:
      print(f'{self.name} is already eating')
      return

    print(f'{self.name} is eating {food}')
    self.is_eating = True

  def stop_eating(self):
    if not self.is_eating:
      print(f'{self.name} is not eating')
      return

    print(f'{self.name} stopped eating')
    self.is_eating = False

  def get_year_of_birth(self):
    year_of_birth = Person.current_year - self.age
    return f'Year of birth: {year_of_birth}'

  @classmethod
  def by_year_of_birth(cls, name, year_of_birth):
    age = cls.current_year - year_of_birth
    return cls(name, age)