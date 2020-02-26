import openpyxl

products = openpyxl.load_workbook('products.xlsx')

sheetnames = products.sheetnames

print(f'Sheetnames: {sheetnames}')

first_spreadsheet = products['Planilha1']

# Head

print(first_spreadsheet['a1'].value)
print(first_spreadsheet['b1'].value)
print(first_spreadsheet['c1'].value)

print('-' * 50)

for field in first_spreadsheet['a']:
  print(field.value)

for field in first_spreadsheet['b']:
  print(field.value)

for field in first_spreadsheet['c']:
  print(field.value)

print('-' * 50)

for row in first_spreadsheet['a1:c4']:
  for column in row:
    print(column.value)

print('-' * 50)

for line in first_spreadsheet:
  print(len(line))

print('-' * 50)

for line in first_spreadsheet:
  if line[0].value is not None:
    print(line[0].value, end=" ")

  if line[1].value is not None:
    print(line[1].value, end=" ")

  if line[2].value is not None:
    print(line[2].value, end=" ")
