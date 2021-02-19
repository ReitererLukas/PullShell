from helperMethods import check_folder, get_parent_dir
import os
from help import change_directory_help

def change_dir(arguments, controller):  
  if len(arguments) == 1:
    
    # check special cases
    if arguments[0] == "..":
      controller.set_current_dir(get_parent_dir(controller.get_current_dir()))
      return
      pass
    elif arguments[0] == "/" or arguments[0] == "\\":
      controller.reset_current_dir()
      return
      pass
    elif arguments[0] == ".": # . wird von os.path.isdir() als Directory erkannt
      return
      pass
    

    if not check_folder(arguments[0]):
      print('  Path is not valid')
      pass
    else:
      controller.set_current_dir(arguments[0])
      pass
    return
    pass

  # change directory to alias (found in saved folders)
  elif len(arguments) == 2 and arguments[0] == 'alias':
    folders = controller.get_folders()
    for f in folders:
      if f.getAlias() == arguments[1]:
        controller.set_current_dir(f.getPath())
        return
        pass
      pass
    print('  Alias not found')
    pass
  print('  Command not found')
  pass

def help():
  change_directory_help()
  pass