def fact(n):
    if n == 1:
        return n
    else:
        return (n)*fact(n-1)
    
n = int(input("Enter a num here: "))
if n<=0:
    print("Factorial of 0 or negative number dosen't exist")
else:
    print("Factorial of the num is: ", fact(n)) 