"""
Program to print all prime numbers between two input numbers using while loop

A program that prompts the user to input two numbers and then finds all the prime numbers between those numbers.
"""

num_1: int = int(input("Enter number_1: "))
num_2: int = int(input("Enter number_2: "))

if num_1 > num_2:
    start: int = num_2
    end: int = num_1
else:
    start: int = num_1
    end: int = num_2

while start <= end:
    if start == 2 or start == 3:
        print(f"{start} is prime")
    elif start < 2 or start % 2 == 0 or start % 3 == 0:
        start += 1
        continue
    else:
        i= 5
        is_prime= 1
        while i * i < start:
            if start % i == 0 or start % i+2 == 0:
                is_prime= 0
                break
            i+= 6
        if is_prime == 1:
            print(f"{start} is prime.")
    start+= 1
