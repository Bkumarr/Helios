#
# Example file for formatting time and date output
#

from datetime import datetime

def main():
  # Times and dates can be formatted using a set of predefined string
  # control codes 
  timenow = datetime.now() # get the current date and time
  
  #### Date Formatting ####
  
  # %y/%Y - Year, %a/%A - weekday, %b/%B - month, %d - day of month
  print (timenow.strftime("The current year is: %Y"))
  print(timenow.strftime("%a %d %B %y"))

  # %c - locale's date and time, %x - locale's date, %X - locale's time
  print(timenow.strftime("THE LOCAL TIME AND DATE: %c"))
 
  print (timenow.strftime("Locale date: %x"))
  print (timenow.strftime("Locale time: %X"))
  #### Time Formatting ####
  
  # %I/%H - 12/24 Hour, %M - minute, %S - second, %p - locale's AM/PM
  print(timenow.strftime("The time format - %I: %M: %S: %p"))
  print(timenow.strftime("Time is %H :%M"))

main();
