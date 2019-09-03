from datetime import datetime, timedelta

FORMAT = '%d/%m/%Y %H:%M:%S'

first_date = datetime.strptime('20/04/1987 20:00:00', FORMAT)
second_date = datetime.strptime('25/04/1987 22:33:00', FORMAT)
diff = second_date - first_date

print(diff)
print(diff.total_seconds())
print(diff.days)
print(second_date > first_date)
print(first_date > second_date)
print(first_date == second_date)
