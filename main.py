
import actions, datetime
from Authentication import auth
from colorama import init; init()
from termcolor import colored

# Variables to be initizialized upon start.

version = "0.0.1_4a"
today = datetime.datetime.now()
#notificationCount = 0 # Currently unimplemented.
#rssCount = 0 # Currently unimplemented.
missingCommand = "--> Error: Command not found, but exists in 'actions' file."

#Displays message if there are any new notifications or RSS messages. Will change functionality later.

"""
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
"""

"""
# Notification settings. Will eventually, like, actually work. Will change functionality later.

if notificationCount > 0:
  notificationCount = colored(notificationCount, "green", attrs = ["blink"])

# RSS settings. Will also eventually, like, actually work. Will change functionality later.

if rssCount > 0:
  rssCount = colored(rssCount, "green")
"""

# Status settings, eventually will be able to tell online/offline status based on network connectivity.

statusOnline = colored("Online", "blue")
statusOffline = colored("Offline", "red")
statusHidden = colored("Hidden", attrs = ["dark"])
status = statusOffline

actions.clear()

print(f"---PyLauncher v{version}---"); print()
actions.motd(); print()

print("--> Enter 'help' for commands."); print()
print(f"Date: {today.month}/{today.day}/{today.year}")
#print(f"Notifications: {notificationCount}")
#print(f"RSS Feeds: {rssCount}")
print(f"Status: {status}"); print()

#print(newMessages)

user = ""

while True:
  command = ""
  command = input(">>> ").lower()

  if command == "":
    pass


  elif command == "login": # This will eventually be used to open a user application that will give all of the options regarding the user status
    user = auth.login()
  

  elif command == "notifications":
    try:
      actions.notifications()
    except AttributeError:
      print(missingCommand)
  

  elif command == "rss":
    try:
      actions.rss()
    except AttributeError:
      print(missingCommand)


  elif command == "applist":
    try:
      actions.applist()
    except AttributeError:
      print(missingCommand)


  elif command == "help":
    try:
      actions.help()
    except AttributeError:
      print(missingCommand)


  elif command == "app_upgrade":
    try:
      actions.app_upgrade()
    except AttributeError:
      print(missingCommand)


  elif command == "runtime_upgrade":
    try:
      actions.runtime_upgrade()
    except AttributeError:
      print(missingCommand)


  elif command == "clear":
    try:
      actions.clear()
    except AttributeError:
      print(missingCommand)


  elif command == "quit" or command == "exit": # Will change later.
    try:
      actions.quit(user)
    except AttributeError:
      print(missingCommand)
    break


  elif command == "test":
    try:
      from Testing import testing
    except ModuleNotFoundError:
      print("--> No testing script was found.")


  else:
    print("--> Invalid command.")
  