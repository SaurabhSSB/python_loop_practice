"""
Program in Python to find the factorial of a given number. Take the number as input.
"""

n: int =int(input("Enter number: "))
fact: int = 1

for i in range(2,n+1):
    fact *= i

print(fact)