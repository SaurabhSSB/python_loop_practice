"""
Program in Python to find whether an input number is a Armstrong number or not.

A program that prompts the user to provide a number and
evaluate whether the number is armstrong number or not.

An Armstrong number is a number that is equal to the sum of its digits,
each raised to the power of the number of digits in the number.
"""

num: str = input("Enter number: ")
digit_count: int = len(num)
addition: int = 0

for digit in num:
    addition += int(digit) ** digit_count

if addition == int(num):
    print(f"{num} is an armstrong number.")
else:
    print(f"{num} is not an armstrong number.")