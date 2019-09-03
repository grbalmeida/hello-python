from datetime import datetime
from locale import setlocale, LC_ALL

setlocale(LC_ALL, 'pt_BR.utf-8')
date = datetime.now()

formatting = date.strftime('%A, %d de %B de %Y')
print(formatting)

formatting = date.strftime('%d/%m/%Y %H:%M:%S')
print(formatting)
