from helperMethods import check_folder, check_file

def check_if_path_alias_exists(argument,files_folders):
  for f in files_folders:
    if f.getAlias() == argument or f.getPath() == argument:
      return f
      pass
    pass
  return None
  pass

def remove_from_cfg_path(path):
  f = open(".\\cfg\\path.txt","r")
  paths = f.read().split("\n")
  paths.remove(path.__str__())
  f.close()
  f = open(".\\cfg\\path.txt","w")
  str_of_paths = ""
  for p in paths:
    str_of_paths += p+"\n"
    pass
  f.write(str_of_paths)
  f.close()
  pass

def remove(argument, files, folders):
  path = check_if_path_alias_exists(argument,files+folders)
  if path == None:
    print('  Alias or Path not found')
    return
    pass
  remove_from_cfg_path(path)
  if check_file(path.getPath()):
    files.remove(path)
    pass
  else:
    folders.remove(path)
    pass
  pass

def remove_path(arguments, files, folders):
  if len(arguments) == 1:
    if arguments[0] == "help":
      help()
      return
      pass
    inp = ""
    while inp != "Y" and inp != "N" and inp != "y" and inp != "n":
      inp = input("Do you wanna do continue?[Y/N] ")
      pass
    if inp == "Y" or inp == "y":    
      remove(arguments[0], files, folders)
      pass
    pass
  elif len(arguments) == 2:
    if arguments[0] == "-f":
      remove(arguments[1], files, folders)
      pass
    pass
  pass

def help():
  print("  rmp argument [path|alias]- remove path")
  print("    -f - deletes without asking")
  pass