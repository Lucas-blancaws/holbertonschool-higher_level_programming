#!/usr/bin/python3

"""read a text file (UTF8)"""


def read_file(filename=""):
    """Reads a file."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
