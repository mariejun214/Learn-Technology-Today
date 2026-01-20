'''
Write a program that divides the restaurant bill by the number of diners 
and shows how much each person must pay.
'''

total_bill = int(input("How much is the total bill? "))
number_of_diners = int(input("How many diners are there? "))

each_person_payment = total_bill / number_of_diners

print("Each diner should pay " + str(each_person_payment) + " each")
