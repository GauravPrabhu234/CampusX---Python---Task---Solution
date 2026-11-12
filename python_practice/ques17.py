# Write a program to read a character and check whether it is an alphabet, digit or special symbol.

char = input("Enter a alphabet/symbol/digit : ")

if char.isalpha():
    print("The character is an alphabet")
elif char.isdigit():
    print("The character is a number.")
else:
    print("The character is a symbol")
