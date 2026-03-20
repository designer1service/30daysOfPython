# Date time 

import datetime
print(dir(datetime))

# Getting datetime Information

from datetime import datetime
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.minute
second = now.second
timestamp = now.timestamp()
print(day, month, year, hour, minute)
print('timestamp', timestamp)
print(f'{day}/{month}/{year}, {hour}:{minute}')

# Formatting Date Output Using strftime
new_year = datetime(2020,1,1)
print(new_year)
day = new_year.day
month = new_year.month
year = new_year.year
hour = new_year.hour
minute = new_year.minute
second = new_year.second
print(day, month, year, hour, minute)
print(f'{day}/{month}/{year}, {hour}:{minute}')

now = datetime.now()
t = now.strftime("%H:%M:%S")
print(t)
time_one = now.strftime("%m/%d/%Y, %H:%M:%S")
print(time_one)
time_two = now.strftime("%d/%m/%Y, %H:%M:%S")
print(time_two)

# String to Time Using strptime

date_string = "5 December, 2019"
print("date_string =", date_string)    
date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object) 

# Using date from datetime

from datetime import date
d = date(2020,1,1)
print(d)
print(d.today())
today = d.today()
print(today.year)
print(today.month)
print(today.day)

# Time Objects to Represent Time

from datetime import time
a = time()
print("a =", a)     # a = 00:00:00
b = time(10, 30, 50)
print("b =", b)     # b = 10:30:50
c = time(hour=10, minute=30, second=50)
print("c =", c)     # c = 10:30:50
d = time(10, 30, 50, 200555)
print("d =", d)     # d = 10:30:50.200555

# Difference Between Two Points in Time Using

today = date(year=2026, month=3, day=20)
new_year = date(year=2027, month=1, day=1)
time_left_for_newyear = new_year - today
print('Time left for new year: ', time_left_for_newyear)

# Difference Between Two Points in Time Using timedelta
from datetime import timedelta
t1 = timedelta(weeks=12, days=10, hours=4, seconds=20)
print(t1)
t2 = timedelta(days=7, hours=5, minutes=3, seconds=30)
print(t2)
t3 = t1 - t2
print("t3 =", t3)

# Exercises: Day 16

# 1
now = datetime.now()
day = now.day
month = now.month
year = now.year
hour = now.hour
minute = now.hour
print(day,month,year)
timestamp = now.timestamp()
print(timestamp)

# 2 
strp = now.strftime("%m/%d/%Y, %H:%M:%S")
print(strp)

# 3
string = '5 December, 2019'
strp= datetime.strptime(string, "%d %B, %Y")
print(type(strp))

# 4 
today = date(year=now.year, month=now.month, day=now.day)
new_year = date(year=2027, month=1, day=1)
t3 = new_year - today
print(t3)

# 5 
today = date(year=now.year, month=now.month, day=now.day)

string = '1 January, 1970'
rnd_date= datetime.strptime(string, "%d %B, %Y")
rnd_date = date(year=rnd_date.year, month=rnd_date.month, day=rnd_date.day)
t3 = today - rnd_date
print(t3)

