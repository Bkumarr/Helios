#
# Example file for working with Calendars
#
from datetime import datetime 
from datetime import date

import calendar

# create a plain text calendar
c = calendar.TextCalendar(calendar.SUNDAY)
str = c.formatmonth(2017, 1, 0, 0)
print (str)

# #    May 2021
# Su Mo Tu We Th Fr Sa
#                    1
#  2  3  4  5  6  7  8
#  9 10 11 12 13 14 15
# 16 17 18 19 20 21 22
# 23 24 25 26 27 28 29
# 30 31

# create an HTML formatted calendar
hc = calendar.HTMLCalendar(calendar.SUNDAY)
str = hc.formatmonth(2017, 1)
print (str)

# loop over the days of a month
# zeroes mean that the day of the week is in an overlapping month
for i in c.itermonthdays(2017, 8):
  print (i)
  
# The Calendar module provides useful utilities for the given locale,
# such as the names of days and months in both full and abbreviated forms
for name in calendar.month_name:
  print (name)

for day in calendar.day_name:
  print (day)

# Calculate days based on a rule: For example, consider
# a team meeting on the first Friday of every month.

print(datetime.date(datetime.now()))
print(datetime.now())
# Team meetings will be on:
#    January  1
#   February  5
#      March  5
#      April  2
#        May  7
#       June  4
#       July  2
#     August  6
#  September  3
#    October  1
#   November  5
#   December  3
