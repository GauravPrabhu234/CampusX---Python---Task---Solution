#  Write a program to read seconds and convert them into hours, minutes and seconds.

# 1. Get the total seconds from the user
total_seconds = int(input("Enter the number of seconds: "))

# 2. Calculate hours and find the leftover seconds
hours = total_seconds // 3600
leftover_seconds = total_seconds % 3600

# 3. Calculate minutes and final seconds from the leftover seconds
minutes = leftover_seconds // 60
seconds = leftover_seconds % 60

# 4. Display the result
print(f"{hours} Hours, {minutes} Minutes, and {seconds} Seconds")
