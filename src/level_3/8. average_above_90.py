"""
Program in Python to print the average of marks of each student only if the average is more than 90

A program that traverses through the list of students and
displays the average of student if average marks above 90.
"""

d = {"Samarth":[45, 60, 50, 90, 70],
     "Jatin": [90, 95, 93, 91, 90],
     "Nishant":[93, 99, 98, 97, 91]}

for i in d:
    average: float = sum(d[i])/len(d[i])
    if average > 90:
        print(f"{i} has average of {average} marks.")