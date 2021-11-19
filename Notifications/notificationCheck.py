from colorama import init; init()
from termcolor import colored

notificationCount = 0 # Currently unimplemented.
rssCount = 0 # Currently unimplemented.

#Displays message if there are any new notifications or RSS messages. Will change functionality later.

newMessages = ""
if notificationCount + rssCount == 0:
  newMessages = colored("<!> No new messages.", "blue")
if notificationCount + rssCount == 1:
  newMessages = colored("<!> You have a new message.", "green")
if notificationCount + rssCount >= 2:
  newMessages = colored("<!> You have new messages.", "green")
if notificationCount + rssCount >= 25:
  newMessages = colored("<!> You have a bunch of new messages.", "yellow")
if notificationCount + rssCount >= 200:
  newMessages = colored("<!> You have a very large number of new messages.", "red")

# Notification settings. Will eventually, like, actually work. Will change functionality later.

if notificationCount > 0:
  notificationCount = colored(notificationCount, "green", attrs = ["blink"])

# RSS settings. Will also eventually, like, actually work. Will change functionality later.

if rssCount > 0:
  rssCount = colored(rssCount, "green")