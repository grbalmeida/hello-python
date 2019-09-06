from string import Template
from datetime import datetime

path = 'useful-modules/string-template'

with open(f'{path}/template.html', 'r') as html:
  template = Template(html.read())
  current_date = datetime.now().strftime('%d/%m/%Y %H:%M:%S')
  page_body = template.substitute(name='Luiz Otavio', date=current_date, title='Template')

with open(f'{path}/new_template.html', 'w') as new_template:
  new_template.write(page_body)
