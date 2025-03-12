"""
Program to print all the multiples of 2 and 7 between 30 and 300

A program that prints multiples of 2 and 7 starting from 30 upto 300.
"""

print("All multiples of 2 and 7 starting from 30 upto 300 are:")
for num in range( 30, 301):
    if num % 2 == 0 or num % 7 == 0:
        print(num, end= " ")