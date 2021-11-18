
import os;

def clear():
  clear = "cls";
  if os.name == "posix":
    clear = "clear";
  os.system(clear);

def applist():
  print("This command currently isn't implemented.");