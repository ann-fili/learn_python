
#Напечатайте в консоль даты: вчера, сегодня, 30 дней назад
#Превратите строку "01/01/25 12:10:03.234567" в объект datetime

from datetime import timedelta
import datetime

dt_today = datetime.datetime.today() #сегодня
print(dt_today)

delta = timedelta(days=1) #вчера
print(dt_today - delta)

delta = timedelta(days=30) # 30 дней назад
print(dt_today - delta)

from datetime import datetime

date_string = '01/01/25 12:10:03.234567'
date_dt = datetime.strptime(date_string, '%y/%m/%d %H:%M:%S.%f')
print(date_dt)

