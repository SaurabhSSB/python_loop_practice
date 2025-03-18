"""
Program to print all the factors of a given input number

A program that prompts the user for an integer and then displays all the factors of that number.
"""

n: int = int(input("Enter a number: "))

for i in range(1,n+1):
    if n % i == 0:
        print(i, end= " ")