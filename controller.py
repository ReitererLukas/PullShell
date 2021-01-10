import os
import classes
from add import add_Path
from ls import list_path
from rmp import remove_path
from help import list_help

blacklisted_signs = ['!','"','§','$','%','&','/','(',')','=','{','[',']','}','?','\',"´",','*','+','~','#',"'",'.',':',',',';','|','>','<']
folders = []
files = []
history = classes.History()

def remove_empty_slots(arr):
  while arr.count('')>0:
    arr.remove('')
    pass
  return arr; 

def execute_command(command, arguments):
 
  arguments = remove_empty_slots(arguments)
  #print(f".{command}.")
  #print(arguments)
  #print(command_list)
  
  try:
    command_list[command](arguments)
    command += ''.join(' '+argument for argument in arguments)
    history.add_to_history(command)
    history.reset_counter()
  except KeyError:
    print('  Command not found')
  pass

def help(arguments):
  list_help()
  pass

def add(arguments):
  file_folder = add_Path(arguments, files, folders)
  if file_folder[0] is not None:
    files.append(file_folder[0])
    pass
  elif file_folder[1] is not None:
    folders.append(file_folder[1])
    pass
pass

def list_all_paths(arguments):
  list_path(arguments,files,folders)
  pass

def rmp(argruments):
  remove_path(argruments, files, folders)
  pass


def load_paths_from_cfg():
  f = open(".\\cfg\\path.txt","r")
  paths = f.read().split("\n")
  for p in paths:
    if p != '':
      arguments = p.split(' ')
      arguments = remove_empty_slots(arguments)
      file_folder = add_Path(arguments=arguments, saved=True)
      if file_folder[0] is not None:
        files.append(file_folder[0])
        pass
      elif file_folder[1] is not None:
        folders.append(file_folder[1])
        pass
    pass
  f.close
  pass


command_list = {"help": help, "add": add, "list": list_all_paths, "rmp": rmp}