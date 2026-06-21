num1 = int(input("Enter your first num: "))
num2 = int(input("Enter your second num: "))

print("Select 1 for addition \nSelect 2 for substracion \nSelect 3 for multiplication \nSelect 4 for devision")
choice = int(input("Enter your choice to get result: "))

if choice == 1:
    print("Sum of the given num is:", num1 +num2)
elif choice == 2:
    print("Substraction of the given num is:", num1-num2)
elif choice == 3:
    print("Multiplication of the given number is:",num1 * num2)
elif choice == 4:
    print("Division of the given num is:",num1 % num2)
else:
    print("Please select the correct option")