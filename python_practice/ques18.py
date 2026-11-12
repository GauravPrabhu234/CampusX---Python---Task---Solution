# Write a program to read the marks of a student and print the grade (A/B/C/D/Fail).

marks = int(input("Enter your marks"))


if marks > 90 :
    print("Congratulations!!! you have passed and secured A grade")
elif marks >  85 :
    print("You have passed and secured B grade")
elif marks > 65 :
    print("You can score more and you have got C grade")
elif marks > 45 :
    print("You need to study hard you got D grade")
else:
    print("Please study well and reappear , You have failed")

