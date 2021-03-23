# imports for Type hinting
from __future__ import annotations
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from .path import Path

# other imports
import os
from platform import system

# alle verbotenen Zeichen
blacklisted_signs: list = ['!', '"', '§', '$', '%', '&', '/',
                                '(', ')', '=', '{', '[', ']', '}', '?', '\\',"´","'", '*', '+', '~', '#', "'", '.', ':', ',', ';', '|', '>', '<']


# checkt on path ein directory ist 
def check_folder(path: str) -> bool:
    return os.path.isdir(path)


# checkt ob path ein file ist
def check_file(path: str) -> bool:
    return os.path.isfile(path)


# speichert einen File in path.txt
def save_to_cfg_path(path: str):
    f = open(".\\cfg\\path.txt", "a")
    f.write(path+"\n")
    f.close()
    pass


# checkt ob Alias bereits existiert und ob er illegale Zeichen beinhaltet
def check_alias(alias: str, files: list[Path], folders: list[Path]) -> bool:
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


# schaut ob der alias oder path exisitiert und returnt den Path 
def check_if_path_alias_exists(argument: str, files_folders: list[Path]) -> Path:
    for f in files_folders:
        if f.getAlias() == argument or f.getPath() == argument:
            return f
            pass
        pass
    return None
    pass


# returnt parent directory of a directory
def get_parent_dir(dir: str) -> str:
    # bestimmt Trennzeichen des pfades
    splitter: str = "\\" if system() == "Windows" else "/" 
    tokens: list[str] = dir.split(splitter)

    # bestimmt, ob dir überhaupt parentDir hat
    if len(tokens) == 2 and tokens[1] == '':
        return dir
        pass
    
    # return parent dir
    return "".join(
        f"{tokens[i]}{splitter if i < len(tokens)-2 or i == 0 else ''}"for i in range(0, len(tokens)-1))
    pass
