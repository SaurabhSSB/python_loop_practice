"""
Program to count the number of distinct elements in a list without using sets

A program that traverses a list and displays the number of distinct elements.
"""

a: list = [1, 2, 2, 3, 4, 4, 5]
a_new: list = []

for num in a:
    if num not in a_new:
        a_new.append(num)

print(len(a_new))