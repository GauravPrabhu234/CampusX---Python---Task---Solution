#  Write a program to find the sum of all even numbers from 1 to n.

n = int(input("Enter your number : "))
sum = 0
for i in range(1,n+1):
    if i%2 == 0:
        sum = sum + i 
print(sum)