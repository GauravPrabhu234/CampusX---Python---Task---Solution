# 30. Write a program to display all multiples of a number m up to n terms.

m = int(input("Enter a number : "))
n = int(input("Enter a number : "))

for i in range(1 , n+1):
     mul = m * i
     print(f"{m} * {i} = {mul} ")

