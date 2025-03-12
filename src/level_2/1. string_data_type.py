"""
Program in Python to print only the string datatype from a list

A program that traverses a given list and displays all the string datatype.
"""

a: list = ["Samarth", "Kunal", "Jatin", 12, 75.5]

for string in a:
    if type(string) == str:
        print(string)