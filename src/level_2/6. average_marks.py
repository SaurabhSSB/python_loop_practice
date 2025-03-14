"""
Program in Python to calculate the average of the marks for each student and print it

A program that takes a given dictionary of marks and evaluates the average marks of each key.
"""

d: dict = {"Samarth":[45, 60, 50, 70], "Jatin": [90, 95, 93, 91, 90], "Nishant":[93, 99, 98, 97, 91]}

for student in d:
    count: int = 0
    addition: float = 0
    for marks in d[student]:
        count += 1
        addition += marks
    print(f"Average marks for {student} is {addition / count}.")