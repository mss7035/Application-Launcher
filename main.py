
import actions, datetime
from Authentication import auth
from colorama import init; init()
from termcolor import colored

# Variables to be initizialized upon start.

today = datetime.datetime.now()
notificationCount = 0 # Currently unimplemented.
rssCount = 0 # Currently unimplemented.

missingCommand = "--> Error: Command not found."

# Status settings, eventually will be able to tell online/offline status based on network connectivity.

statusOnline = colored("Online", "blue", attrs = ["blink"])
statusOffline = colored("Offline", "red")
statusHidden = colored("Hidden", attrs = ["dark"])
status = statusOffline

actions.clear()

# Version of the program. Set every time there is a new update!

version = "0.0.1_3a"

print(f"---PyLauncher v{version}---"); print()
actions.motd(); print()

print("--> Enter 'help' for commands."); print()
print(f"Date: {today.month}/{today.day}/{today.year}")
#print(f"Notifications: {notificationCount}")
#print(f"RSS: {rssCount}")
print(f"Status: {status}"); print()

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

  elif command == "quit": # Will change later.
    if user == "":
      print("Exit.")
    else:
      print(f"Exit user '{user}'.")
    break

  elif command == "test":
    try:
      import testing
    except ModuleNotFoundError:
      print("--> No testing script was found.")

  else:
    print("--> Invalid command.")
  