from datetime import datetime

date = datetime.strptime('20/04/2019', '%d/%m/%Y')
print(date.timestamp())

date = datetime.fromtimestamp(1555729200.0)
print(date)
