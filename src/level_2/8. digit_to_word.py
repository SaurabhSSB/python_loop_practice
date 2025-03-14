"""
Program to print the digits of an input number in word format

A program that prompts the user to input a number and display it's digit one by one in english format.
"""

num: str = input("Enter number: ")
num_eng: dict = {"1": "One", "2": "Two", "3": "Three", "4": "Four", "5": "Five", "6": "Six", "7": "Seven",
                 "8": "Eight", "9": "Nine"}

for digit in num:
    if digit in num_eng:
        print(num_eng[digit])