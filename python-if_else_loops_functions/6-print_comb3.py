#!/usr/bin/python3
for i in range(10):
    for j in range(i + 1, 10):  # j commence à i+1, donc j > i toujours
        if i == 8 and j == 9:
            print(f"{i}{j}")
        else:
            print(f"{i}{j}, ", end="")
