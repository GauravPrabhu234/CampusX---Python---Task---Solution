# Write a program to read the marks of 5 subjects and print the total and average.

maths = int(input("Enter the marks of maths : "))
english = int(input("Enter the marks of english : "))
geography = int(input("Enter the marks of geography : "))
hindi = int(input("Enter the marks of hindi : "))
marathi = int(input("Enter the marks of marathi : "))

total = maths + english + geography + hindi + marathi
print(f"The total marks of 5 subject is {total}")

avg = (maths + english + geography + hindi + marathi)/5
print(f"The average of 5 subject is {avg}")
