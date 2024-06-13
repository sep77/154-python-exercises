import time
from datetime import datetime
from datetime import datetime, timedelta
# from time import gmtime, strftime
# import datetime

# 96- print current date and time in python.
# print(datetime.datetime.now())
# or
# print(datetime.datetime.now().time())

# Method2
# print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))


# 97- convert string into a datetime object

date_string = "Feb 25 2020 4:20PM"

datetime_object = datetime.strptime(date_string, "%b %d %Y %I:%M%p")
print(datetime_object)


# 98- subtract a week from a given date.
given_date = datetime(2100, 2, 25)

days_to_subtract = 7

result = given_date - timedelta(days=days_to_subtract)
print(result)


# 99- print a date in the following format.
# Day_name  Day_number  month_name  Year

given_date = datetime(2100, 12, 15)

date = given_date.strftime("%A %d %B %Y")
print(date)


# 100- Find the day of the week of a given date.

given_date = datetime(2100, 12, 15)

print(given_date.today().weekday())

print(given_date.strftime("%A"))


# 101- Add a week and 12 hours to a given date.

given_date = datetime(2050, 3, 15, 10, 0, 0)

result = given_date + timedelta(days=7, hours=12)
print(result)


# 102- print current time in milliseconds.
print(int(round(time.time() * 1000)))


# 103- calculate the date 4 months from the given date.

given_date = datetime(2035, 5, 20).date()

# from datetime import datetime  # from dateutil.relativedelta import relativedelta

# result = given_date + relativedelta(months = 4)


# 104- calculate number of days between two given dates.

date_1 = datetime(2050, 2, 25)
date_2 = datetime(2065, 9, 17)

delta = None

if (date_1 > date_2):
    print("date_1 is greater")
    delta = date_1 - date_2

else:
    print("date_2 is greater")
    delta = date_2 - date_1

print("Number of Days:", delta.days)
