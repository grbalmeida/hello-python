from datetime import datetime
from calendar import mdays

date = datetime.now()
current_month = int(date.strftime('%m'))
print(current_month)
print(mdays)
print(mdays[current_month])