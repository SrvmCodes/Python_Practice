num = int(input("Enter your number: "))
sum=0
if num<0:
    print("Please enter positive number")
else:
    while num>0:
        sum =sum+num
        num -= 1
    print(sum)