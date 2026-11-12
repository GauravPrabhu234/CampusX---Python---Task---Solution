# Write a program to read a number and check whether it is divisible by both 3 and 5.

num = int(input("Enter a number : "))
if num %3 == 0 and num % 5 == 0 :
    print("The number is divisble by both 3 and 5")
else:
    print("The number is not divisible")