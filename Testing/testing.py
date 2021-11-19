import os

path = "/home/runner/Application-Launcher/Testing/database.txt"

if os.path.exists(path):
  print("That location exists.")
  if os.path.isfile(path):
    print("That is a file.")
  elif os.path.isdir(path):
    print("That is a directory.")
else:
  print("That location doesn't exist.")


text = "Egg.\nOh, by the way, your text has been overwritten."

egg = "\nGuess who just got added to the text file?"

with open("database.txt", "w") as file:
  file.write(text)

with open("database.txt", "a") as file:
  file.write(egg)






def password(username):
  password = input(f"Set password for '{username}': ")
  while True:
    if len(password) <= 7:
      print("Password is too short, try again.")
      password()
    else:
      return password()

"""
def register():
  db = open("database.txt", "r")
  username = input("New username: ").lower()
  d = []
  f = []
  for i in db:
    a, b = i.split(", ")
    b = b.strip()
    d.append(a)
    f.append(b)
  data = dict(zip(d, f))
  if username in d:
    print(f"User by '{username}' already exists, try another username.")
    register()
  else:
    password = password(username)
"""

#register()