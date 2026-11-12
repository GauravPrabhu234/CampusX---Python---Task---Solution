# Write a program to read three numbers and find the largest among them.

a = int(input("Enter a number : "))
b = int(input("Enter a number : "))
c = int(input("Enter a number : "))

if a > b and a > c :
    print("A is the largest")
elif b > a and b > c :
    print("B is the largest")
else :
    print("C is the largest")