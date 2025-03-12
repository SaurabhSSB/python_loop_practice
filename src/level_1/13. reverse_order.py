"""
Program in Python that accepts a word from the user and prints the characters of the word in reverse fashion.
"""

word: str = input("Enter word: ")
rev_word: str = ""

for count in range(1, len(word)+1):
    rev_word: str = rev_word + word[-count]

print(rev_word)

