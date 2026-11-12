# Write a program to read the radius of a circle and print its area and circumference.

rad = float(input("Enter the radius of the circle : "))

area = 3.14 * rad **2
print(f"The area of circle with radius {rad} is {area}")

circum = 2 * 3.14 * rad
print(f"The circumference of the circle with radius {rad} is {circum}")