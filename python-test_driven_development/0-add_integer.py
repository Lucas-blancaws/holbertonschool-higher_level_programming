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

    if isinstance(a, float) and (
        a == float("inf") or a == float("-inf") or a != a
    ):
        raise OverflowError("a is too large or not a finite number")

    if isinstance(b, float) and (
        b == float("inf") or b == float("-inf") or b != b
    ):
        raise OverflowError("b is too large or not a finite number")

    return int(a) + int(b)
