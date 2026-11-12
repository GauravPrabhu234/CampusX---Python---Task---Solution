# Write a program to read the length and breadth of a rectangle and print its area and perimeter.

len = float(input("Enter the length of rectangle : "))
breadth = float(input("Enter the breadth of rectangle : "))

area = len * breadth
print(f"The area of rectange is {area}")

perim = 2 * (len + breadth)
print(f"The perimeter of rectangle is {perim}")