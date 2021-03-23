# imports for Type hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller import Controller

# other imports
from utils.__init__ import *
from commands.help import change_directory_help


# called function
def change_dir(arguments: list, controller: Controller):
    if len(arguments) == 1:

        # aufruf von help
        if arguments[0] == "help":
            controller.set_output(help())
            return 
            pass

        # check special cases -> no directory
        # wechnselt ins parent Dir
        elif arguments[0] == "..":
            controller.set_current_dir(
                get_parent_dir(controller.get_current_dir()))
            return
            pass

        # ins root Verzeichnis wechseln
        elif arguments[0] == "/" or arguments[0] == "\\":
            controller.reset_current_dir()
            return
            pass

        # bleibt im gleichen directory
        elif arguments[0] == ".":
            # do nothing
            return
            pass

        # überprüft, ob angegebener dir auch valid ist
        if not check_folder(arguments[0]):
            controller.set_output('  Path is not valid')
            pass
        else:
            controller.set_current_dir(arguments[0])
            pass
        return
        pass

    # change directory to alias (found in saved folders)
    elif len(arguments) == 2 and arguments[0] == 'alias':
        folders: list[Path] = controller.get_folders()

        # sucht folder mit dem alias
        for f in folders:
            if f.getAlias() == arguments[1]:
                controller.set_current_dir(f.getPath())
                return
                pass
            pass

        # wenn kein passender Path gefunden wurde
        controller.set_output('  Alias not found')
        pass

    # no argument match
    controller.set_output('  Command not found')
    pass


# helper Methode
def help() -> str:
    return change_directory_help()
    pass
