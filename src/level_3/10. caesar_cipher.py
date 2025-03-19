"""
Program to implement a Caesar Cipher encryption using a for loop, where n represents the number of shifts for each letter in the alphabet

Prompts the user for a string and then shifts the position of the alphabet by n and displays the string.
Caesar Cipher - Each alphabet is shifted by n positions.
"""

word: str = input("Enter the string: ")
word_caesar_cipher: str= ""
n: int = int(input("Caesar Cipher value: "))

for i in range(len(word)):
    if  97 <=ord(word[i]) + n <= 122:
        x: int = ord(word[i]) + n
        word_caesar_cipher= word_caesar_cipher + chr(x)
    else:
        x: int = ord(word[i]) + n - 26
        word_caesar_cipher = word_caesar_cipher + chr(x)

print(word_caesar_cipher)