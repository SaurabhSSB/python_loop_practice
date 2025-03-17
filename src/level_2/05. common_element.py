"""
Program in Python to print the common elements between two lists

A program to traverse and display the elements that are same in two given lists.
Ordered should be maintained.
"""

li1: list =[10, 20, 50, 80, 60]
li2: list = [50, 88, 95, 76, 81, 10, 60, 50, 60]

for num in li1:
    if num in li2:
        print(num, end=" ")