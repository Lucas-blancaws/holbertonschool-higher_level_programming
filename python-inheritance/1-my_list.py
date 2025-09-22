#!/usr/bin/python3
"""Module 1-my_list: MyList class"""


class MyList(list):
    """List subclass with print_sorted method"""

    def print_sorted(self):
        """Print the list in ascending order"""
        print(sorted(self))
