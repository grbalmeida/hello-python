class Database:
  def __init__(self):
    self.__data = {}

  @property
  def data(self):
    return self.__data

  def insert_customer(self, id, name):
    if 'customers' not in self.__data:
      self.__data['customers'] = {id: name}
    else:
      self.__data['customers'].update({id: name})

  def list_customers(self):
    for id, name in self.__data['customers'].items():
      print(id, name)

  def delete_customer(self, id):
    del self.__data['customers'][id]

db = Database()
db.insert_customer(1, 'Otavio')
db.insert_customer(2, 'Miranda')
db.insert_customer(3, 'Rose')
db.delete_customer(2)
db.list_customers()

print(db.data)
db.__data = 'str'
print(db.__data)
print(db._Database__data)
