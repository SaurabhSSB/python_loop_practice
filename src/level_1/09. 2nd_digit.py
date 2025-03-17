"""
Program to print the 2nd digit

A program that traverses a tuple and displays the 2nd digit of all numbers.
"""

t: tuple = (23, 45, 67, 90, 12, 10)

for num in t:
    if num > 9:
        print(f"2nd digit of {num} is {str(num)[1]}.")
    else:
        print(f"2nd digit is not available in {num}.")