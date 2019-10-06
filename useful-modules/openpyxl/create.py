import openpyxl
from random import uniform

spreadsheet = openpyxl.Workbook()
spreadsheet.create_sheet('Spreadsheet1', 0)
spreadsheet.create_sheet('Spreadsheet2', 0)

first_spreadsheet = spreadsheet['Spreadsheet1']
second_spreadsheet = spreadsheet['Spreadsheet2']

for line in range(1, 11):
  order_id = line - 1
  first_spreadsheet.cell(line, 1).value = order_id
  first_spreadsheet.cell(line, 2).value = 1200 + line
  price = round(uniform(10, 100), 2)
  first_spreadsheet.cell(line, 3).value = price

for line in range(1, 11):
  second_spreadsheet.cell(line, 1).value = f'Luiz {line} {round(uniform(10, 100), 2)}'
  second_spreadsheet.cell(line, 2).value = f'Otavio {line} {round(uniform(20, 200), 2)}'
  second_spreadsheet.cell(line, 3).value = f'John {line} {round(uniform(30, 300), 2)}'

spreadsheet.save('new-spreadsheet.xlsx')
