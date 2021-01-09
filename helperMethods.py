import os

def check_folder(path):
  return os.path.isdir(path)

def check_file(path):
  return os.path.isfile(path)

def save_to_cfg_path(path):
  f = open(".\\cfg\\path.txt","a")
  f.write(path+"\n")
  f.close()
  pass

def check_alias(alias):
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