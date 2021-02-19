from history import History
from path import Path
from add import add_Path
from list_path import list_path
from removePath import remove_path
from help import list_help
from changeDir import change_dir
from platform import system
from os.path import normpath

class Controller:
  
  # Constructor für den Controller
  def __init__(self):
    self.__blacklisted_signs = ['!','"','§','$','%','&','/','(',')','=','{','[',']','}','?','\',"´",','*','+','~','#',"'",'.',':',',',';','|','>','<']
    self.__folders = []
    self.__files = []
    self.__command_list = {}
    self.__history = History()
    self.reset_current_dir() # setzt das aktuelle working Directory
    pass

  # entfernt aus dem arguments array alle Elemente
  # die nicht beinhalten 
  def remove_empty_slots(self,arr):
    while arr.count('')>0:
      arr.remove('')
      pass
    return arr; 

  # ruft die Methoden für die einzelnen Commands auf
  # arguments ist ein Array, welches alle Wörter (aus der eingabe,
  # getrennt bei Leerzeichen) beinhaltet
  # Weiters added er die commands auch in die History
  def execute_command(self,command, arguments):
  
    arguments = self.remove_empty_slots(arguments)
    
    try:
      self.__command_list[command](arguments)
      command += ''.join(' '+argument for argument in arguments)
      self.__history.add_to_history(command)
      self.__history.reset_counter()
    except KeyError:
      print('  Command not found - in command list')
    pass

  # ruft funktion mit den Help-prints auf
  def help(self,arguments):
    list_help()
    pass

  # aufruf des add Commands
  def add(self,arguments):
    add_Path(arguments, self)
  pass

  # aufruf des list Commands
  def list_all_paths(self,arguments):
    list_path(arguments,self)
    pass

  # aufruf des rmp (remove Path) Commands
  def rmp(self,argruments):
    remove_path(argruments, self)
    pass

  # aufruf des cd Commands
  def cd(self, arguments):
    change_dir(arguments, self)
    pass

  # Man ladet die gespeicherten Pfade aus der cfg Datei ins Programm
  def load_paths_from_cfg(self):
    f = open(".\\cfg\\path.txt","r")
    paths = f.read().split("\n")
    for p in paths:
      if p != '':
        arguments = p.split(' ')
        arguments = self.remove_empty_slots(arguments)

        add_Path(controller=self, arguments=arguments, saved=True)
      pass
    f.close
    pass

  # diese Methode registriert alle  commands
  def register_commands(self):
    self.__command_list.update({
      "help": self.help, 
      "add": self.add, 
      "list": self.list_all_paths, 
      "rmp": self.rmp,
      "cd": self.cd})
    pass

  # liefert das aktuelle working directory zurück
  def get_current_dir(self):
    return self.__current_dir
    pass

  # setzt das aktuelle working directory
  # wird vor der Command eingabe eingeblendet
  def set_current_dir(self, dir):
    self.__current_dir = normpath(dir)
    pass

  # resets the current directory
  def reset_current_dir(self):
    # platform.system() überprüft das OS
    self.__current_dir = 'C:\\' if system() == 'Windows' else '/'

  # returnt alle Files
  def get_files(self):
    return self.__files
    pass

  # fügt 1 File in die Liste ein
  def add_file(self, file):
    self.__files.append(file)
    pass
  
  # löscht ein File aus der Liste
  def delete_file(self,file):
    self.__files.remove(file)
    pass
  
  # returnt die ganze Folder Liste
  def get_folders(self):
    return self.__folders
    pass

  # fügt 1 Folder in die Liste ein
  def add_folder(self, folder):
    self.__folders.append(folder)
    pass

  # löscht ein Folder aus der Liste
  def delete_folder(self,folder):
    self.__folders.remove(folder)
    pass