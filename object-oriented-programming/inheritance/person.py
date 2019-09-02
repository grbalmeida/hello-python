class Person(object):
  def __init__(self, name, age):
    self.name = name
    self.age = age
    self.class_name = self.__class__.__name__

  def speek(self):
    print(f'{self.class_name} is talking...')
