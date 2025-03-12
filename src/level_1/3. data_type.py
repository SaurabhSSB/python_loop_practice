"""
Program to print the data type of each element in the given tuple.

A program that takes a tuple as an input and displays the type of each element.
"""

t: tuple = ("Someone", 34, "hi", 12.983, 34 +9j)

for data in t:
    print(f"The type of data is {type(data)}.")