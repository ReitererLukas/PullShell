from help import list_path_help

# gibt alle Folder aus
# Indent als Parameter gibt an wie viele Leerzeichen eingerückt ist
def list_folders(indent_multiplier, folders):
  indent = " "*indent_multiplier
  if len(folders) == 0:
    print(f"{indent}List is empty")
    pass
  else:
    for folder in folders:
      print(f"{indent}{folder}")
      pass
    pass
  pass

# gibt alle Files aus
# Indent als Parameter gibt an wie viele Leerzeichen eingerückt ist
def list_files(indent_multiplier, files):
  indent = " "*indent_multiplier
  if len(files) == 0:
    print(f"{indent}List is empty")
    pass
  else:
    for file in files:
      print(f"{indent}{file}")
      pass
    pass
  pass

def list_path(arguments,controller):
  files = controller.get_files()
  folders = controller.get_folders()
  
  if len(arguments) == 1:
    if arguments[0] == "help":
      help()
      return
      pass
    if arguments[0] == "-f":
      list_files(2, files)
      pass
    elif arguments[0] == "-d":
      list_folders(2, folders)
      pass
    elif arguments[0] == "-fd":
      print("  Files")
      list_files(4, files)
      print("  Folders")
      list_folders(4, folders)
      pass
    elif arguments[0] == "-df":
      print("  Folders")
      list_folders(4, folders)
      print("  Files")
      list_files(4, files)
      pass
    else:
      print('  Argument not found')
      pass
    pass
  pass

def help():
  list_path_help()
  pass
