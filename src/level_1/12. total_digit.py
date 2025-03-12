"""
Program in Python to count the total number of digits in a number. Take number as input.
"""

num: str = input("Enter number: ")
add: int = 0

for digit in num:
    add += int(digit)

print(add)