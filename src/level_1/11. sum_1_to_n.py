"""
Program in Python to calculate the sum of all numbers from 1 to n.

Prompts the user to input a number, then evaluate and display sum till that number from 1.
"""

n: int = int(input("Enter number: "))
addition: int = 0

for num in range(n+1):
    addition += num

print(addition)