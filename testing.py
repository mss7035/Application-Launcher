from datetime import date 
today = date.today()
print("Today's date:", today)

###

import datetime

e = datetime.datetime.now()

print ("Current date and time = %s" % e)

print ("Today's date: %s/%s/%s" % (e.month, e.day, e.year))

print ("The time is now: %s:%s:%s" % (e.hour, e.minute, e.second))

###

import time
print (time.strftime("%H:%M:%S"))

###

from colorama import init
from termcolor import colored

# use Colorama to make Termcolor work on Windows too
init()

# then use Termcolor for all colored text output
print(colored('Hello, World!', 'green', 'on_red'))