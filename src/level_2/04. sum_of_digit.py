"""
Program to take a number as input from the user and print the sum of it's digits

A program that prompts the user to provide a number and displays the sum of the digits.
"""

num: str = input("Enter number: ")
digit_count: int = len(num)
addition: int = 0

for digit in num:
    addition += int(digit)

print(f"The sum of digits of {num} is {addition}.")