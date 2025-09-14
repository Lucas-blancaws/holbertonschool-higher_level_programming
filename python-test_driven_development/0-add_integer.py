#!/usr/bin/python3
"""
Module 0-add_integer
Defines a function that adds two integers.
"""
def add_integer(a, b=98):
    """
    Additionne deux entiers.

    Arguments :
        a : Le premier nombre (int ou float).
        b : Le deuxième nombre (int ou float), par défaut 98.

    Return :
        La somme de a et b en tant qu'entier.

    Exceptions :
        TypeError : Si a ou b n'est pas un entier ou un flottant.
        """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
