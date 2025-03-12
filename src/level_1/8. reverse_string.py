"""
Program to reverse a string without using slicing

A program that takes string input form user and displays it's reverse.
"""

string: str = input("Enter a string: ")

for i in range(1,len(string)+1):
    print(string[-i], end= "")