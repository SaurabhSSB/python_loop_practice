"""
Program in Python to check whether two strings are anagrams of each other using only for loops

A program that prompts the user for two strings and evaluates whether the two strings are anagrams or not.
An anagram of a string is another string that contains the same characters, only the order of characters can be different.
"""

str_1: str = input("Enter string_1: ")
str_2: str = input("Enter string_2: ")

list_1: list = list(str_1.lower())
list_2: list = list(str_2.lower())
list_1.sort()
list_2.sort()

print(f"'{str_1}' and '{str_2}' are anagrams is {list_1 == list_2}.")