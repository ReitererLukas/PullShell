# imports for Type hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller import Controller

# other imports
from commands.help import list_path_help


# returnt alle Folder
# Indent_multiplier gibt an, um wie viele Leerzeichen eingerückt wird
def list_folders(indent_multiplier: int, folders: list) -> str:
    indent: str = " "*indent_multiplier

    return f"{indent}List is empty" if len(folders) == 0 else "".join(
        f"{indent}{folder}" + ("\n" if folder is not folders[-1] else "") for folder in folders)
    pass


# returnt alle Files
# Indent_multiplier gibt an, um wie viele Leerzeichen eingerückt wird
def list_files(indent_multiplier: int, files: list) -> str:
    indent: str = " "*indent_multiplier

    return f"{indent}List is empty" if len(files) == 0 else "".join(
        f"{indent}{file}" + ("\n" if file is not files[-1] else "") for file in files)
    pass


# called function
def list_paths(arguments: list, controller: Controller):
    files: list = controller.get_files()
    folders: list = controller.get_folders()

    # Nur ein argument gegeben
    if len(arguments) == 1:

        # aufruf von der help Funktion
        if arguments[0] == "help":
            controller.set_output(help())
            pass

        # checkt ob argument -f ist
        elif arguments[0] == "-f":
            # ruft passende funktion auf
            controller.set_output(list_files(2, files))
            pass

        # checkt on argument -d ist
        elif arguments[0] == "-d":
            # ruft passende funktion auf
            controller.set_output(list_folders(2, folders))
            pass

        # checkt on argument -fd ist
        elif arguments[0] == "-fd":
            # ruft passende funktionen auf
            controller.set_output("".join(["  Files\n", list_files(
                4, files), "\n  Folders\n", list_folders(4, folders)]))
            pass

        # checkt on argument -df ist
        elif arguments[0] == "-df":
            # ruft passende funktionen auf
            controller.set_output("".join(["  Folders\n", list_folders(
                4, folders), "\n  Files\n", list_files(4, files)]))
            pass

        # no match
        else:
            controller.set_output('  Argument not found')
            pass

    # mehr als 1 Argument
    else:
        controller.set_output('  Too many arguments')
        pass
    pass


# helper Methode
def help() -> str:
    return list_path_help()
    pass
