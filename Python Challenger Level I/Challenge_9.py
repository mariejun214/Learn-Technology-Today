'''
Write a program that will convert the numbers of years into months and days.
Ask the user for the number of years and display the number of years and the 
total months, then the total days.
'''
years = int(input("Enter the number of years: "))

months = years * 12
days = years * 365 #note: This is simple conversion, so, Leap year is not included in the computation

print(f"In {years} years there are ... \nTotal of {months} months, \nTotal of {days} days.")
