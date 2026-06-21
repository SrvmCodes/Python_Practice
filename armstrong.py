# ARMSTRONG NUM MEANS
# A number that is equal to the sum of its digits, 
# each raised to the power of the total number of digits.
# 153 = (1*1*1)+(5*5*5)+(3*3*3) = 153
# 12 = (1*1)+(2*2) != 5 [Not Armstrong]
num = int(input("Enter a num to check armstrong or not: "))
# order = len(str(num))  #For a 4_digit input

sum = 0
temp = num   #save num in temp variablel to make changes when needed
while temp > 0:
    digit = temp % 10  #Takes last digit of temp variable
    cube = digit**3
    # cube = digit**order   #WHile solving 4digit num 
    sum = sum + cube
    temp //= 10
if sum == num:
    print("It is an Armstrong num")
else:
    print("It is not an armstrong num")