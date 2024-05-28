import datetime as dt

# datetime is class and now is the method inside datetime class
now = dt.datetime.now()
year = now.year
print(year)
day_of_week = now.weekday()
print(day_of_week)

date_of_birth = dt.datetime(year=2004, month=7 , day=28)
print(date_of_birth)
