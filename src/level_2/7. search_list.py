"""
Program to search if a particular student name/rollno is present in the list or not.
Take name/rollno as input and print the corresponding data.

A program that prompts the user to either provide a name or rollno and then traverse a given list and
display corresponding rollno or name and display Does not Exist for non-existent.
"""

Name = ["Samarth", "Jatin", "Nishant", "Harsg", "Dabru", "Kunal"]
Roll_no = [1, 20, 13, 4, 9, 11]

variable: str = input("Enter the Name or Roll_No.: ")

if variable.isdigit():
    var: int = int(variable)
    if var in Roll_no:
        x: int = Roll_no.index(var)
        print(Name[x])
    else:
        print("Does not exist.")
else:
    if variable in Name:
        y: int = Name.index(variable)
        print(Roll_no[y])
    else:
        print("Does not exist.")