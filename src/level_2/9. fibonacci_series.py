"""
Program to create a fibonacci sequence of n digits

A program that prompts the user to input and number and
displays fibonacci series up till that number.
"""

n: int = int(input("Enter number: "))
x: int = 0
y: int = 1

for i in range(n+1):
    if i == 0:
        print(x)
    elif i == 1:
        print(y)
    else:
        temp= y
        y+= x
        x= temp
        print(y)