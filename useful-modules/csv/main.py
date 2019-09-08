import csv
import sys

argv = sys.argv

def print_customers():
  with open('./customers.csv', 'r') as file:
    data = csv.reader(file)
    next(data)


    for customer in data:
      name, lastname, email, phone = customer

      print(f'Name: {name}')
      print(f'Lastname: {lastname}')
      print(f'Email: {email}')
      print(f'Phone: {phone}')
      print()

def dict_reader():
  with open('./customers.csv', 'r') as file:
    data = csv.DictReader(file)

    for customer in data:
      print(f"Name: {customer['Name']}")
      print(f"Lastname: {customer['Lastname']}")
      print(f"Email: {customer['Email']}")
      print(f"Phone: {customer['Phone']}")
      print()

def new_file():
  with open('./customers.csv', 'r') as file:
    data = [customer for customer in csv.DictReader(file)]

  with open('./new-customers.csv', 'w') as file:
    write = csv.writer(
      file,
      delimiter=',',
      quotechar='"',
      quoting=csv.QUOTE_ALL
    )

    keys = data[0].keys()
    keys = list(keys)

    write.writerow(
      [
        keys[0],
        keys[1],
        keys[2],
        keys[3]
      ]        
    )

    for customer in data:
      write.writerow(
        [
          customer['Name'],
          customer['Lastname'],
          customer['Email'],
          customer['Phone']
        ]        
      )

if '-print_customers' in argv:
  print_customers()

if '-dict_reader' in argv:
  dict_reader()

if '-new_file' in argv:
  new_file()
