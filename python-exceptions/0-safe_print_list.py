#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    compteur = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            compteur += 1
    except IndexError:
        print("depassement taille de liste")
    print()
    return compteur
