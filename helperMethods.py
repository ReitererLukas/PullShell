import os
from os.path import split
from platform import system

blacklisted_signs = ['!','"','§','$','%','&','/','(',')','=','{','[',']','}','?','\',"´",','*','+','~','#',"'",'.',':',',',';','|','>','<']

def check_folder(path):
  return os.path.isdir(path)

def check_file(path):
  return os.path.isfile(path)

def save_to_cfg_path(path):
  f = open(".\\cfg\\path.txt","a")
  f.write(path+"\n")
  f.close()
  pass

def check_alias(alias, files, folders):
  for f in files+folders:
    if f.getAlias() == alias:
      return False
      pass
    pass
  
  for entity in blacklisted_signs:
    if alias.__contains__(entity):
      return False
      pass
    pass

  return True
  pass

def check_if_path_alias_exists(argument,files_folders):
  for f in files_folders:
    if f.getAlias() == argument or f.getPath() == argument:
      return f
      pass
    pass
  return None
  pass

def get_parent_dir(dir):
  splitter = ""

  if system() == 'Windows':
    splitter = "\\"
    pass
  elif system() == 'Linux':
    splitter = "/"
    pass

  tokens = dir.split(splitter)

  if len(tokens) == 2 and tokens[1] == '':
    return dir
    pass

  new_dir = ""
  new_dir += "".join(f"{tokens[i]}{splitter if i < len(tokens)-2 or i == 0 else ''}"for i in range(0,len(tokens)-1)) 
  return new_dir
  pass
