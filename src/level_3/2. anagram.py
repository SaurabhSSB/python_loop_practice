"""
Program in Python to check whether two strings are anagrams of each other using only for loops.

A program that prompts the user for two strings and evaluates whether the two strings are anagrams or not.
An anagram of a string is another string that contains the same characters, only the order of characters can be different.
"""

str_1: str = input("Enter string_1: ")
str_2: str = input("Enter string_2: ")
anagram: int = 1

set_1: set = set(str_1)
set_2: set = set(str_2)

if len(str_1) == len(str_2):
    for char in set_1:
        if char not in set_2:
            anagram= 0
            break
else:
    anagram= 0

if anagram == 0:
    print(f"'{str_1}' and '{str_2}' are not anagrams.")
else:
    print(f"'{str_1}' and '{str_2}' are anagrams.")