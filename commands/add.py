# imports for Type hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller import Controller

# other imports
from utils.__init__ import *
from commands.help import add_help
from os.path import normpath  # wechselt die / auf \


# saves path to cfg file
def save_to_cfg_path(path):
    f = open(".\\cfg\\path.txt", "a")
    f.write(path+"\n")
    f.close()
    pass


# called function: saved -> wird bei startup auf True gesetzt,
# da dort die Paths nicht mehr in path.txt hinzugefügt werden müssen
def add_Path(arguments: list, controller: Controller, saved: bool = False):
    # loggt, on Folder bzw File gültig ist
    valid: bool = False

    # ruft help auf
    if len(arguments) == 1 and arguments[0] == "help":
        controller.set_output(help())
        return
        pass

    # checkt ob path bzw path & alias pair bereits existiert
    if path_alias_pair_exists(controller, arguments):
        controller.set_output("  Path alias pair already exists")
        return

    # add ohne alias
    if len(arguments) == 1:
        # überprüft, ob es ein gültiger Folder ist
        if check_folder(arguments[0]):
            valid = True
            controller.add_folder(Path(normpath(arguments[0])))
            pass

        # überprüft, ob es ein gültiger File ist
        elif check_file(arguments[0]):
            valid = True
            controller.add_file(Path(normpath(arguments[0]), None))
            pass

        # weder gültiges File noch Folder
        else:
            controller.set_output('  Invalid Path')

        # wenn, der Path valid und noch nicht gesaved ist, wird er in path.txt abgespeichert
        if not saved and valid:
            save_to_cfg_path(normpath(arguments[0]))
            pass
        pass

    # add mit alias
    elif len(arguments) == 3 and arguments[1] == "as":
        # überprüft, ob der alias gültig ist
        if not check_alias(arguments[2], controller.get_files(), controller.get_folders()):
            controller.set_output('  Alias not valid')
            return

        # überprüft, ob es ein gültiger Folder ist
        if check_folder(arguments[0]):
            valid = True
            controller.add_folder(Path(normpath(arguments[0]), arguments[2]))
            pass

        # überprüft, ob es ein gültiger File ist
        elif check_file(arguments[0]):
            valid = True
            controller.add_file(Path(normpath(arguments[0]), arguments[2]))
            pass

        # weder gültiges File noch Folder
        else:
            controller.set_output('  Invalid Path')

        # wenn, der Path valid und noch nicht gesaved ist, wird er in path.txt abgespeichert
        if not saved and valid:
            save_to_cfg_path(normpath(arguments[0])+" as "+arguments[2])
            pass
        pass

    # Command not found - aber nur wenn die funktion, vom
    # User aufgerufen wird ==> saved = false
    elif not saved:
        controller.set_output('  Command not found')
        pass
    pass


# checkt ob path bzw {path & alias pair} bereits existiert
def path_alias_pair_exists(controller: Controller, argruments: list) -> bool:
    files: list[Path] = controller.get_files()
    folders: list[Path] = controller.get_folders()

    # überprüfung, wenn kein alias angegeben ist
    if len(argruments) == 1:
        for f in files+folders:
            if f.getAlias() == '' and f.getPath() == argruments[0]:
                return True
                pass
            pass
        pass

    # überprüfung, wenn ein alias angegeben ist
    elif len(argruments) == 3:
        for f in files+folders:
            if f.getAlias() == argruments[2] and f.getPath() == argruments[0]:
                return True
                pass
            pass
        pass

    # returnt False, wenn der path bzw path alias pair noch nicht existiert
    return False
    pass


# helper Method
def help() -> str:
    return add_help()
    pass
