from platform import system

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

print(get_parent_dir("D:\\000_Programmieren"))