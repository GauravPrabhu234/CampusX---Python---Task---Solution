a = 1
sum = 0
x = int(input("Enter your number : "))
n = int(input("Enter your number : "))
for i in range(1,n+1):
    sum = sum + a **3/x
    a+=2
    print(f"sum of series is {sum}")
