"""
Program to print all the two digit even numbers which are also a multiple of 3.

A program that prints all even two digit multiple of 3.
"""

print("All even two digit multiple of 3 are:")

for num in range(10, 99, 2):
    if num % 3 == 0:
        print(num, end = " ")