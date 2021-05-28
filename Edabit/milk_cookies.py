# Xmas Eve is almost upon us, prepare milk and cookies for Santa. Create a function
# that accepts a Date object and returns True if it's Xmas Eve (Dec. 24) and False
# otherwise.
import datetime
def time_for_milk_and_cookies(date):
    return (date.month == 12 and date.day == 24)

a = time_for_milk_and_cookies(datetime.date(2013, 12, 24))
print(a)

a = time_for_milk_and_cookies(datetime.date(2013, 1, 23))
print(a)

a = time_for_milk_and_cookies(datetime.date(3000, 12, 24))
print(a)

a = time_for_milk_and_cookies(datetime.date(2023, 12, 5))
print(a)
