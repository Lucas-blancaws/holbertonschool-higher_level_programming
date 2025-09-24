#!/usr/bin/python3
"""Module 3-is_kind_of_class: defines is_kind_of_class function"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or a subclass of a_class
    otherwise False.
    """
    return isinstance(obj, a_class)
