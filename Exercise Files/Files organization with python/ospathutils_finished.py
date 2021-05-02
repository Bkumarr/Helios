#
# Example file for working with os.path module
#

import os
from os import path
import datetime
from datetime import date, time, timedelta
import time

def main():
  # Print the name of the OS
  print (os.name)
  
  # Check for item existence and type
  print ("Item exists: " + str(path.exists("textfile.txt")))
  print ("Item is a file: " + str(path.isfile("textfile.txt")))
  print ("Item is a directory: " + str(path.isdir("textfile.txt")))
  
  # Work with file paths
  print ("Item's path: " + str(path.realpath("textfile.txt")))
  print ("Item's path and name: " + str(path.split(path.realpath("textfile.txt"))))
  
  # Get the modification time
  t = time.ctime(path.getmtime("textfile.txt"))
  print (t)
  print (datetime.datetime.fromtimestamp(path.getmtime("textfile.txt")))
  
  # Calculate how long ago the item was modified
  td= datetime.datetime.now() - datetime.datetime.fromtimestamp(path.getmtime("textfile.txt"))
  print ("It has been " + str(td) + " since the file was modified")
  print ("Or, " + str(td.total_seconds()) + " seconds")

# ls_start.py
# posix
# Item exists: True
# Item is a file: True
# Item is a directory: False
# Item's path: /home/runner/Tutorial/Exercise Files/Ch4/textfile.txt
# Item's path and name: ('/home/runner/Tutorial/Exercise Files/Ch4', 'textfile.txt')
# Sun May  2 16:24:06 2021
# 2021-05-02 16:24:06.342763
# It has been 0:10:18.494144 since the file was modified