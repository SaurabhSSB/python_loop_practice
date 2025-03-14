""""
Program to convert a decimal number to binary number

A program that prompts the user to provide a number and then prints the binary of that number.
"""

num: int= int(input("Enter number: "))
q: int= num
binary: str= ""
while num // 2 != 0:
    binary += str(num % 2)
    num //= 2
binary+= "1"
print(binary[::-1])
