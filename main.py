
import actions;
from Authentication import auth;

# Variables to be initizialized upon start.
notImplemented = "(Currently not implemented.)";

actions.clear();

# Version of the program. Set every time there is a new update!
version = "0.0.1_2a"

print(f"""---Application Launcher v{version}---
""")
print("""--> This is the first version of this software
    and is FAR from complete, although this is a project
    that may last indefintely so we will see how this goes.

--> An RSS feed will be displayed up here at some point,
    along with the data and time and perhaps notifications.
""");
print("--> Enter 'help' for commands."); print();
print(f"Time: {notImplemented}");
print(f"Notifications: {notImplemented}");
print(f"RSS: {notImplemented}"); print();

user = "";

while True:
  command = "";
  command = input(">>> ").lower();

  if command == "":
    pass;

  elif command == "login": # This will eventually be used to open a user application that will give all of the options regarding your user status
    user = auth.login();


  elif command == "applist":
    actions.applist();

  elif command == "clear":
    actions.clear();

  elif command == "quit": # Will change later.
    if user == "":
      print("Exit.");
    else:
      print(f"Exit user '{user}'.");
    break;

  else:
    print("Invalid command.")
  
