from itertools import groupby

students = [
  {'name': 'Luiz', 'grade': 'A'},
  {'name': 'Leticia', 'grade': 'C'},
  {'name': 'Fabricio', 'grade': 'B'},
  {'name': 'Rosemary', 'grade': 'D'},
  {'name': 'Joana', 'grade': 'A'},
  {'name': 'Joao', 'grade': 'E'},
  {'name': 'Eduardo', 'grade': 'A'},
  {'name': 'Andre', 'grade': 'B'},
  {'name': 'Anderson', 'grade': 'A'},
  {'name': 'Jose', 'grade': 'C'},
]

order = lambda student: student['grade']
students.sort(key=order)
grouped_students = groupby(students, order)

for grouping, grouped_values in grouped_students:
  print(f'Grouping: {grouping}')
  quantity = len(list(grouped_values))
  print(f'\t{quantity} students got the grade {grouping}')
