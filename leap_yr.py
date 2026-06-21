year = int(input("Enter a year: "))
# This condition is for century years
if (year % 400 == 0) and (year % 100 == 0):
    print("This is a leap year")
# This condition is for normal years
elif (year % 4 == 0) and (year % 100 != 0):
    print ("This is a leap year") 
else:
    print("Thsi is definately not a leap year")