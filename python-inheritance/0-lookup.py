#!/usr/bin/python3
"""Module 0-lookup: contains the function lookup"""


def lookup(obj):
    """
    Return a list of available attributes and methods of `obj`.
    """
    return list(dir(obj))
