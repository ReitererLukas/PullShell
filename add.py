from path import Path
from helperMethods import check_folder, check_file, check_alias
from help import add_help
from os.path import normpath # wechselt die / auf \

def save_to_cfg_path(path):
  f = open(".\\cfg\\path.txt","a")
  f.write(path+"\n")
  f.close()
  pass

# add *path* [as *alias*]
def add_Path(arguments, controller, saved = False):
  valid = False

  if len(arguments) == 1 and arguments[0] == "help":
    help()
    return
    pass

  if path_alias_pair_exists(controller, arguments):
    print("  Path alias pair already exists")
    return

  if len(arguments) == 1:
    if check_folder(arguments[0]):
      valid = True
      controller.add_folder(Path(normpath(arguments[0])))
      pass
    elif check_file(arguments[0]):
      valid = True
      controller.add_file(Path(normpath(arguments[0]),None))
      pass

    if not saved and valid:
      save_to_cfg_path(normpath(arguments[0]))
      pass
    pass

  elif len(arguments) == 3 and arguments[1] == "as":
    if not check_alias(arguments[2], controller.get_files(), controller.get_folders()):
      print('  Alias not valid')
      return

    if check_folder(arguments[0]):
      valid = True
      controller.add_folder(Path(normpath(arguments[0]), arguments[2]))
      pass
    elif check_file(arguments[0]):
      valid = True
      controller.add_file(Path(normpath(arguments[0]), arguments[2]))
      pass

    if not saved and valid:
      save_to_cfg_path(normpath(arguments[0])+" as "+arguments[2])
      pass
    pass

  # Command not found - aber nur wenn die funktion, vom
  # User aufgerufen wird ==> saved = false
  elif not saved:
    print('  Command not found')
    pass
  pass

def path_alias_pair_exists(controller, argruments):
  files = controller.get_files()
  folders = controller.get_folders()

  if len(argruments) == 1:
    for f in files+folders:
      if f.getAlias() == '' and f.getPath() == argruments[0]:
        return True
        pass
      pass
    pass
  
  elif len(argruments) == 3:
    for f in files+folders:
      if f.getAlias() == argruments[2] and f.getPath() == argruments[0]:
        return True
        pass
      pass
    pass

  return False
  pass

def help():
  add_help()
  pass
