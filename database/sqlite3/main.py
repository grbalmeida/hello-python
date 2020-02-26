import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()

cursor.execute(
  'DROP TABLE customers'        
)

cursor.execute(
  'CREATE TABLE customers ('
    'id INTEGER PRIMARY KEY AUTOINCREMENT,'
    'name TEXT,'
    'weight REAL'
  ')'
)

cursor.execute(
  'DELETE FROM customers'        
)

cursor.execute(
  'INSERT INTO customers (name, weight) VALUES (?, ?)',
  ('Maria', 50)
)

cursor.execute(
  'INSERT INTO customers (name, weight) VALUES (?, ?)',
  ('Daniel', 89)
)

cursor.execute(
  'INSERT INTO customers (name, weight) VALUES (:name, :weight)',
  {'name': 'John', 'weight': 56}
)

cursor.execute(
  'INSERT INTO customers (name, weight) VALUES (:name, :weight)',
  {'name': 'Luiz Otavio', 'weight': 78}
)

cursor.execute(
  'UPDATE customers SET name=:name WHERE id=:id',
  {'name': 'Maria da Silva', 'id': 1}
)

cursor.execute(
  'UPDATE customers SET name=:name WHERE id=:id',
  {'name': 'Daniel Rodrigues', 'id': 2}
)

cursor.execute(
  'DELETE FROM customers WHERE id=:id',
  {'id': 3}
)

cursor.execute(
  'DELETE FROM customers WHERE id=:id',
  {'id': 4}
)

connection.commit()

cursor.execute('SELECT * FROM customers')

for line in cursor.fetchall():
  customer_id, name, weight = line
  print(f'Customer id: {customer_id}')
  print(f'Name: {name}')
  print(f'Weight: {weight}')
  print('-' * 50)

cursor.close()
connection.close()
