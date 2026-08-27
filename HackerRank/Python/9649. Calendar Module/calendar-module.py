# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
import datetime

month, day,year = map(int,input().split())

day_i = calendar.weekday(year,month,day)
day_name  = calendar.day_name[day_i].upper()

print(day_name)
