'''
Write a program that adds the user's numbers.
Set the total to 0 to start with. While the total is 50 or less, ask the user to input a number. Add that number to the total and
print the message

“The total is… [total]”.

Stop the loop when the total is 50 or over 50.
'''
total = 0

print("Let's add your numbers")

while total < 50:
    number = int(input("Add a number: "))
    total += number
    print("The total is " + str(total))
    