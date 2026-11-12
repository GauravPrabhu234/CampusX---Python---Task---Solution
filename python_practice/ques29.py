#  Write a program to display the multiplication table of a number n.

n = int(input("Enter the number : "))


for i in range(1,11):
    mul = n * i
    print(f"{n} * {i} = {mul} ")