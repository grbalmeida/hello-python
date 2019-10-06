import openpyxl
from random import uniform

products = openpyxl.load_workbook('products.xlsx')
first_spreadsheet = products['Planilha1']
first_spreadsheet['A1'].value = 'OrderId'
first_spreadsheet['B1'].value = 'ProductId'
first_spreadsheet['C1'].value = 'Price'

for line in range(5, 16):
  first_spreadsheet.cell(line, 1).value = line
  first_spreadsheet.cell(line, 2).value = 1200 + line

  price = round(uniform(10, 100), 2)

  first_spreadsheet.cell(line, 3).value = price

products.save('new-products.xlsx')
