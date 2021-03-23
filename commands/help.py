# imports for Type hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from controller import Controller

# ruft alle Helpfunktionen auf
def list_help(controller: Controller) -> str:
    output = ""
    output = "".join(["", quit_help(), "\n"])
    output = "".join([output, add_help(), "\n"])
    output = "".join([output, list_path_help(), "\n"])
    output = "".join([output, remove_path_help(), "\n"])
    output = "".join([output, help_help(), "\n"])
    output = "".join([output, change_directory_help()])
    controller.set_output(output)
    pass


# Quit
def quit_help() -> str:
    return "  q - Quit"
    pass


# add Path
def add_help() -> str:
    return "  add path {as alias} - add a Path"
    pass


# list paths
def list_path_help() -> str:
    ret = "".join(["  list argument - list content", "\n"])
    ret = "".join([ret, "    -d - list saved paths to directories", "\n"])
    ret = "".join([ret, "    -f - list saved paths to files", "\n"])
    ret = "".join([ret, "    -fd - list saved paths to files and directories", "\n"])
    ret = "".join([ret, "    -df - list saved paths to directories and files"])
    return ret
    pass


# remove path
def remove_path_help() -> str:
    ret = "".join(["  rmp argument [path|alias] - remove path", "\n"])
    ret = "".join([ret, "    -f - deletes without asking"])
    return ret
    pass


# help
def help_help() -> str:
    ret = "".join(["  help - lists all available commands", "\n"])
    ret = "".join([ret, "  {command} help - lists all information about the command"])
    return ret
    pass


# change directory
def change_directory_help() -> str:
    ret = "".join(["  cd - goes back to the home directory", "\n"])
    ret = "".join([ret, "    path - changes the working directory", "\n"])
    ret = "".join([ret, "    alias Alias - changes to the directory of the save alias", "\n"])
    ret = "".join([ret, "    .. - goes a directory up", "\n"])
    ret = "".join([ret, "    / - goes back to the root directory"])
    return ret
    pass
