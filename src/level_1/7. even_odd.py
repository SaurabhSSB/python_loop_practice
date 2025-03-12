"""
Program to print even/odd for all the numbers

A program that traverses a tuple and displays even/odd along with the numbers.
"""

t = (23, 45, 67, 90, 12, 10)

for num in t:
    if num % 2 == 0:
        print(f"{num}: even")
    else:
        print(f"{num} : odd")