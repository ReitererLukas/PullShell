# ruft alle Helpfunktionen auf
def list_help():
  quit_help()
  add_help()
  list_path_help()
  remove_path_help()
  help_help()
  change_directory_help()
  pass

def quit_help():
  # Quit
  print("  q - Quit")
  pass

def add_help():
  # add Path
  print("  add path {as alias} - add a Path")
  pass

def list_path_help():
  # list content
  print("  list argument - list content")
  print("    -d - list saved paths to directories")
  print("    -f - list saved paths to files")
  print("    -fd - list saved paths to files and directories")
  print("    -df - list saved paths to directories and files")
  pass

def remove_path_help():
  # remove path
  print("  rmp argument [path|alias] - remove path")
  print("    -f - deletes without asking")
  pass

def help_help():
  # help
  print("  help - lists all available commands")
  print("  {command} help - lists all information about the command")
  pass

def change_directory_help():
  #change directory
  print("  cd - goes back to the home directory")
  print("    path - changes the working directory")
  print("    alias Alias - changes to the directory of the save alias")
  print("    .. - goes a directory up")
  print("    / - goes back to the root directory")
  pass