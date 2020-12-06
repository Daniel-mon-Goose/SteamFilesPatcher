import os
import sys
from typing import Iterable

import keyboard

from context import ContextInterface, KF1Context


def print_introduction(cntx: ContextInterface) -> None:
    if cntx.desc is not None:
        print(cntx.desc)
    if cntx.prerequisites is not None:
        print(cntx.prerequisites)


def get_path_to_game_directory(directories_seq: Iterable[str]) -> str:
    steam: str = input("Enter the path to your local Steam directory: ")
    return os.path.join(steam, *directories_seq)


def key_press_exit(exit_code: int, message: str = None) -> None:
    if message is not None:
        print(message)
    print(">>> Press Enter to exit...")
    keyboard.wait("Enter")
    sys.exit(exit_code)


def modify_file_contents(file_name: str, abs_path: str, cntx: ContextInterface) -> None:
    file_data: str = ""
    try:
        with open(os.path.join(abs_path, file_name), "r") as fin:
            file_data = fin.read()

        for old, new in cntx.replacements.items():
            file_data = file_data.replace(old, new)

        with open(os.path.join(abs_path, file_name), "w") as fout:
            fout.write(file_data)
    except FileNotFoundError:
        key_press_exit(1, message=f"\nError: although the provided path is correct, {file_name} is missing.\n"
                                  f"Try to verify integrity of your game files.\n"
                       )


def main(cntx: ContextInterface) -> None:
    print_introduction(cntx)

    path: str = get_path_to_game_directory(cntx.directories_chain)
    while not os.path.exists(path):
        print("Error: the correct path to local Steam directory is required "
              "or your game is absent from your installed library\n")
        path = get_path_to_game_directory(cntx.directories_chain)

    for name in cntx.filenames:
        modify_file_contents(name, path, cntx)

    key_press_exit(0, message=cntx.success)


if __name__ == "__main__":
    main(KF1Context())
