#!/usr/bin/python3
"""Module 2-is_same_class: defines is_same_class function"""


def is_same_class(obj, a_class):
    """
    Return True if obj is exactly an instance of a_class,
    otherwise False.
    """
    return type(obj) is a_class
