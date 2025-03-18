"""
Program to print all possible pairs of elements from a list using nested for loops

A program that traverses a list and displays the pair of all possible pairs of the elements of list.
"""

a: list = [1, 2, 3]
a_set: set = set(a)
a_list: list = list(a_set)

for i in range(len(a_list)):
    for j in range(i, len(a_list)):
        print(a_list[i] , a_list[j])