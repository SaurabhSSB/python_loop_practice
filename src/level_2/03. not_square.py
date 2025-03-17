"""
Program in python to print the sum of only those keys from the dictionary for which the value is NOT a square of the keys

A program that traverses through a given dictionary and
display the keys where the value are not it's square.
"""

d: dict = {5:16, 3:9, 10:81, 1:0, 6:36}

for key in d:
    if key ** 2 != d[key]:
        print(f"{key} which has the value {d[key]} in it.")