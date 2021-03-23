# imports for Type hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller import Controller

# other imports
from utils.__init__ import *
from commands.help import remove_path_help
from os.path import normpath


# entfernt Path aus path.txt
def remove_from_cfg_path(path: Path):
    f = open(".\\cfg\\path.txt", "r") # öffnet file im read modus
    paths = f.read().split("\n") # splittet content nach Zeilenumbruch
    paths.remove(path.__str__()) # entfernt den path
    f.close()

    f = open(".\\cfg\\path.txt", "w") # öffnet file im write modus
    # stöpselt die übrigen Paths wieder zusammen
    str_of_paths = ""
    for p in paths:
        if p != "":
            str_of_paths += p+"\n"
            pass
        pass
    f.write(str_of_paths) # schreibt paths wieder
    f.close()
    pass


# handlet das löschen des Paths
def remove(argument: list, controller: Controller):
    files = controller.get_files()
    folders = controller.get_folders()

    # checkt, ob der path überhaupt existiert
    path = check_if_path_alias_exists(argument, files+folders)
    if path == None:
        controller.set_output('  Alias or Path not found')
        return
        pass

    # entfent path aus path.txt
    remove_from_cfg_path(path)

    # entfernet entweder aus files oder folders
    if check_file(path.getPath()):
        files.remove(path)
        pass
    else:
        folders.remove(path)
        pass
    pass


# wird vom Controller aus aufgerufen
# checkt ob eine Sicherungs-Frage benötigt wird oder nicht
def remove_path(arguments: list, controller: Controller):
    
    # wenn 1 Argument übergeben wird
    # => entweder help oder löschen mit Frage
    if len(arguments) == 1:
        # help
        if arguments[0] == "help":
            controller.set_output(help())
            return
            pass

        # auf gültige Eingabe warten
        inp = ""
        while inp != "Y" and inp != "N" and inp != "y" and inp != "n":
            inp = controller.ask_question("Do you wanna do continue?[Y/N]")
            pass
        # bei Übereinstimmung löschen aufrufen
        if inp == "Y" or inp == "y":
            remove(normpath(arguments[0]), controller)
            pass
        pass

    # 2 Argumente
    elif len(arguments) == 2:
        # -f: sicherheitsFrage wird übergangens
        if arguments[0] == "-f":
            remove(normpath(arguments[1]), controller)
            pass
        pass
    pass


#helper method
def help() -> str:
    return remove_path_help()
    pass
