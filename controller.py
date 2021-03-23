from utils.__init__ import *
from platform import system
from os.path import normpath
from interfaces.thread_interface import IThread

#Command imports
from commands.__init__ import *

class Controller:

    # Constructor für den Controller
    def __init__(self):
        self.__blacklisted_signs: list = ['!', '"', '§', '$', '%', '&', '/',
                                    '(', ')', '=', '{', '[', ']', '}', '?', '\',"´",', '*', '+', '~', '#', "'", '.', ':', ',', ';', '|', '>', '<']
        self.__folders: list = []
        self.__files: list = []
        self.__command_list = {}
        self.__history: History = History()
        self.reset_current_dir()  # setzt das aktuelle working Directory
        self.__is_output_set: bool = False
        pass

    # entfernt aus dem arguments array alle Elemente
    # die nichts beinhalten
    def remove_empty_slots(self, arr: list):
        while arr.count('') > 0:
            arr.remove('')
            pass
        return arr

    # ruft die Methoden für die einzelnen Commands auf
    # arguments ist ein Array, welches alle Wörter (aus der eingabe,
    # getrennt bei Leerzeichen) beinhaltet
    # Weiters added er die commands auch in die History
    def execute_command(self, command: str, arguments: list):

        arguments = self.remove_empty_slots(arguments)
        self.__is_output_set = False
        try:
            self.__command_list[command](arguments)
            command += ''.join(' '+argument for argument in arguments)
            self.__history.add_to_history(command)
            self.__history.reset_counter()
        except KeyError:
            self.__thread.set_output('  Command not found - in command list')
        pass

    # ruft funktion mit den Help-prints auf
    def help(self, arguments: list):
        list_help(self)
        self.set_output(mode = False) if not self.__is_output_set else ""
        pass

    # aufruf des add Commands
    def add(self, arguments: list):
        add_Path(arguments, self)
        self.set_output(mode = False) if not self.__is_output_set else ""
    pass

    # aufruf des list Commands
    def list_all_paths(self, arguments: list):
        list_paths(arguments, self)
        self.set_output(mode = False) if not self.__is_output_set else ""
        pass

    # aufruf des rmp (remove Path) Commands
    def rmp(self, argruments: list):
        remove_path(argruments, self)
        self.set_output(mode = False) if not self.__is_output_set else ""
        pass

    # aufruf des cd Commands
    def cd(self, arguments: list):
        change_dir(arguments, self)
        self.set_output(mode = False) if not self.__is_output_set else ""
        pass

    # Man ladet die gespeicherten Pfade aus der cfg Datei ins Programm
    def load_paths_from_cfg(self):
        f = open(".\\cfg\\path.txt", "r")
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
    def get_current_dir(self) -> str:
        return self.__current_dir
        pass

    # setzt das aktuelle working directory
    # wird vor der Command eingabe eingeblendet
    def set_current_dir(self, dir: str):
        self.__current_dir = normpath(dir)
        pass

    # resets the current directory
    def reset_current_dir(self):
        # platform.system() überprüft das OS
        self.__current_dir = 'C:\\' if system() == 'Windows' else '/'
        pass

    # returnt alle Files
    def get_files(self) -> list:
        return self.__files
        pass

    # fügt 1 File in die Liste ein
    def add_file(self, file: Path):
        self.__files.append(file)
        pass

    # löscht ein File aus der Liste
    def delete_file(self, file: Path):
        self.__files.remove(file)
        pass

    # returnt die ganze Folder Liste
    def get_folders(self) -> list:
        return self.__folders
        pass

    # fügt 1 Folder in die Liste ein
    def add_folder(self, folder: Path):
        self.__folders.append(folder)
        pass

    # löscht ein Folder aus der Liste
    def delete_folder(self, folder: Path):
        self.__folders.remove(folder)
        pass

    def set_output(self, output: str = "", mode: bool = True):
        self.__is_output_set = True
        self.__thread.set_output(output,mode)
        pass

    def set_thread(self, thread: IThread):
        self.__thread = thread
        pass

    # stellt eine Frage und returnt die Antwort
    def ask_question(self, question:str) -> str:
        return self.__thread.ask_question(question)
        pass

    pass
