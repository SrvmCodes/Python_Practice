num = int(input("Enter your number: "))
if num == 1:
    print("Number is not prime")
if num > 1:
    for i in range (2, num):
        if num % i == 0:
            print("Number is not prime")
            break
    else:
        print("Number is a prime")
        
