"""
maintenance/main.py _(Version 3)_
--------------------------------------------

Author: Matthew

Description: Maintenance toolkit for DoomMapGuessr's Image Library.

DateCreated: 29/03/2026 @ 19:34

Compatibility: Compatible with MAPDAT4.db only.

--------------------------------------------

License: MIT _(see below)_

> MIT License
>
> Copyright (c) 2026 Matthew
>
> Permission is hereby granted, free of charge, to any person obtaining a copy
> of this software and associated documentation files (the "Software"), to deal
> in the Software without restriction, including without limitation the rights
> to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the Software is
> furnished to do so, subject to the following conditions:
>
> The above copyright notice and this permission notice shall be included in all
> copies or substantial portions of the Software.
>
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
> IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
> FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
> AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
> LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
> OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
> SOFTWARE.
"""

# [*] Imports
import csv
import os
import platform
import re
import sqlite3
import subprocess
from argparse import ArgumentParser
from collections import defaultdict
from pathlib import Path

import requests
from core import connection
from utils import add_images_to_db as imgadd

# [*] Constants
CONFIG: str = ""

DIFFICULTY_NAMES: list[str] = [
    "I'm too Young to Guess",
    "Guessing: not too rough",
    "Guess me Plenty",
    "Ultra-Guessing",
    "Guessmare!",
    "Guessmare!! PLUS",
]

DIFFICULTY_ABBREVIATION: list[str] = ["ITYTG", "GNTR", "GMP", "UG", "GM", "GM+"]


def get_full_difficulty_name(difficulty_level: int) -> str:
    """
    get_full_difficulty_name

    Returns the difficulty in the form of a string such as `<name> (<abbreviation>)`.

    :param int difficulty_level: the difficulty level to get (from 1 to 6, both ends included)
    :return str: the string described above
    """

    return f"{DIFFICULTY_NAMES[difficulty_level - 1]} ({DIFFICULTY_ABBREVIATION[difficulty_level - 1]})"


if __name__ == "__main__":
    parser = ArgumentParser("DoomMapGuessr MAPDAT4 [Maintenance Kit]")
    subparsers = parser.add_subparsers(dest="command")

    parser.add_argument("database", type=str, help="Path to the MAPDAT4 database file.")

    add_command = subparsers.add_parser("add", help="Add images to MAPDAT4")
    add_command.add_argument(
        "sel",
        type=str,
        help="Selection of images to add: can be a single image path, a list of paths separated by '?' or '*' for all images.",
    )
    add_command.add_argument(
        "mapid",
        type=int,
        help="ID of the map that matches the images to add.",
    )
    add_command.add_argument(
        "--recursive",
        action="store_true",
        help="When using sel='*', this option allows for recursive lookup.",
    )

    args = parser.parse_args()

    match args.command:
        case "add":
            images: list[tuple[Path, float, float, str]] = []

            if args.sel == "*":
                images = imgadd.find_all_image_files_to_add(Path.cwd(), args.recursive)

            elif "?" in args.sel:
                paths = [Path(i) for i in args.sel.split("?")]
                images = imgadd.find_image_files_to_add(paths)

            else:
                images = imgadd.find_image_files_to_add([args.sel])

            conn = connection.get_connection(args.database)

            if not conn:
                print("!! error: no connection (None)")
                exit()

            try:
                errors = imgadd.add_images_to_database(conn, args.mapid, images)

            except Exception as ex:
                print(f"!! error: {ex} !!")

            else:
                print(errors)

            finally:
                conn.close()

        case _:
            pass
