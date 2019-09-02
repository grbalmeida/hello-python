from person import Person

class Customer(Person):
  def buy(self):
    print(f'{self.class_name}')
