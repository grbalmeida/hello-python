import sqlite3

class Contacts:
  def __init__(self, file):
    self.connection = sqlite3.connect(file)
    self.cursor = self.connection.cursor()

  def insert(self, name, phone):
    query = 'INSERT OR IGNORE INTO contacts (name, phone) VALUES (?, ?)'
    self.cursor.execute(query, (name, phone))
    self.connection.commit()

  def update(self, name, phone, contact_id):
    query = 'UPDATE OR IGNORE contacts SET name = ?, phone = ? WHERE contact_id = ?'
    self.cursor.execute(query, (name, phone, contact_id))
    self.connection.commit()

  def delete(self, contact_id):
    query = 'DELETE FROM contacts WHERE contact_id = ?'
    self.cursor.execute(query, (contact_id,))
    self.connection.commit()

  def fetchall(self):
    self.cursor.execute('SELECT * FROM contacts')

    for line in self.cursor.fetchall():
      contact_id, name, phone = line
      print(f'Contact id: {contact_id}')
      print(f'Name: {name}')
      print(f'Phone: {phone}')
      print('-' * 40)

  def close(self):
    self.cursor.close()
    self.connection.close()

if __name__ == '__main__':
  contacts = Contacts('database.db')
  contacts.fetchall()
