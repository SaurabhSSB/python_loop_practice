"""
Program to print the sum of individual tuples separately.

A program that traverses through a list and prints the sum of all the individual tuples.
"""

marksList: list = [(23, 24, 31), (56, 34, 53), (42, 58, 31)]

for tup in marksList:
    value: int= 0
    for item in tup:
        value += item
    print(f"{tup} sum is {value}.")
