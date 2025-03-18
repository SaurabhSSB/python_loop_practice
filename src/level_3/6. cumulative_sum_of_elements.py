"""
Program to create a list of the cumulative sum of elements of a given list using for loops

A program that takes a list and displays the cumulative sum of elements of list.
"""

a: list = [1, 2, 3, 4]
add: int = 0
add_list: list = []

for i in a:
    add+= i
    add_list.append(add)

print(add_list)