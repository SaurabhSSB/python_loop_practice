"""
Program to calculate the sum of the product of corresponding elements from two lists

A program that traverses two lists and displays the sum of product of corresponding elements.
"""

a: list = [1, 2, 3]
b: list = [4, 5, 6,]
add: int = 0

if len(a)>len(b):
    end: int = len(b)
else:
    end: int = len(a)

for i in range(end):
    add+= a[i] * b[i]

print(add)