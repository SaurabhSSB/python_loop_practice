"""
Program to print the first and last character of all the names in the given list

A program that traverses a given list of names and prints the first and last character.
"""

l:list = ["Mayank", "Aniket", "Saurabh", "Rahul"]
for i in l:
    print(f"first character: {i[0]} and last character: {i[-1]}.")
