from classes import Path
from helperMethods import check_folder, check_file, check_alias

def save_to_cfg_path(path):
  f = open(".\\cfg\\path.txt","a")
  f.write(path+"\n")
  f.close()
  pass

# add *path* [as *alias*]
def add_Path(arguments, saved = False):
  valid = False
  file_folder = (None,None)
  if len(arguments) == 1:
    if arguments[0] == "help":
      help()
      return (None,None)
      pass
    
    if check_folder(arguments[0]):
      valid = True
      file_folder = (None,Path(arguments[0]))
      pass
    elif check_file(arguments[0]):
      valid = True
      file_folder = (Path(arguments[0],None))
      pass

    if not saved and valid:
      save_to_cfg_path(arguments[0])
      pass
    pass

  elif len(arguments) == 3 and arguments[1] == "as":
    if not check_alias(arguments[2]):
      print('  Alias not valid')
      return

    if check_folder(arguments[0]):
      valid = True
      file_folder = (None, Path(arguments[0], arguments[2]))
      pass
    elif check_file(arguments[0]):
      valid = True
      file_folder = (Path(arguments[0], arguments[2]),None)
      pass

    if not saved and valid:
      save_to_cfg_path(arguments[0]+" as "+arguments[2])
      pass
    pass

  else:
    print('  Command not found')
    pass
  return file_folder
  pass

def help():
  print("  add path {as alias} - add a Path")
  pass
