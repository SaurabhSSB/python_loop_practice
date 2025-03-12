"""
Program to print all the numerical data

A program that traverses a list and prints all numerical data.
"""

l: list= [2, 5, "a", 5, "r", 7, "m", "t", "4"]

for item in l:
    if isinstance(item, (int, float, complex)):
        print(f"{item} is numerical data.")
    elif isinstance(item, str) and item.isdigit():
        print(f"{item} is numerical data present as string.")

