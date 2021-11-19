
import os

notImplemented = "--> This command currently isn't implemented."

def motd():
  try:
    with open("motd.txt") as file:
      print(file.read())
  except FileNotFoundError:
    print("Error: MOTD not found.")


def applist():
  print(notImplemented)


def help():
  try:
    with open("guide.txt") as file:
      print(file.read()); print()
  except FileNotFoundError:
    print("--> No guide present."); print()


def app_upgrade():
  print(notImplemented)


def runtime_upgrade():
  print(notImplemented); print()
  if os.name == "nt":
    print("--> The updater does not support Windows.")
  else:
    distribution = input("--> Which distribution do you use?: ")
    if distribution == "":
      print("--> Please enter your Linux distribution")
      runtime_upgrade()
    elif distribution == "debian":
      os.system("sudo apt update python3")
    elif distribution == "macos" or distribution == "mac":
      print("--> MacOS is currently unsupported.")
    elif distribution == "windows":
      print("--> No you don't.")
    else:
      print("--> Either this Linux distribution isn't listed or doesn't exist."); print()


def clear():
  clear = "cls"
  if os.name == "posix":
    clear = "clear"
  os.system(clear)


def quit(user):
    if user == "":
      print("Exit.")
    else:
      print(f"Exit user '{user}'.")