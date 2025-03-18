"""
Program to flatten a nested list (i.e., a list of lists) into a single list using for loops

A program that traverses a nested list and displays the elements one by one.
"""

a: list = [[1,2], [3,4,5],[6]]

for element in a:
    for i in element:
        print(i, end= " ")