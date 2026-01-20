'''
Write a program that will convert the numbers of days into hours, minutes, and seconds.

Ask the user for the desired number of days and display the days, then convert them to 
hours, minutes, and seconds.
'''

days = int(input("Enter the number of days: "))

hours = days * 24
minutes = days * 24 * 60
seconds = days * 24 * 60 * 60

print(f"In {days} days there are...\n{hours} total hours \n{minutes} total minutes \n{seconds} total seconds")

