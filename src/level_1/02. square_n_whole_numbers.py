"""
Program to print the powers of first n whole numbers

A program that prompts the user to input a number and the power they want the output to have and
program prints the power of the whole number till the number given by user.
"""

n: int = int(input("Enter the number: "))
p: int = int(input("Enter the power: "))

for num in range(n+1):
    print(f"{num} to the power {p} is {num ** p}.")