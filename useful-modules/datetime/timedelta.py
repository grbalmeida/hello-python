from datetime import datetime, timedelta

FORMAT = '%d/%m/%Y %H:%M:%S'

date = datetime.strptime('20/04/1987 20:00:00', FORMAT)

date = date + timedelta(days=5)
print(date.strftime(FORMAT))

date = date + timedelta(weeks=40)
print(date.strftime(FORMAT))

date = date + timedelta(minutes=600)
print(date.strftime(FORMAT))

date = date + timedelta(hours=24)
print(date.strftime(FORMAT))
