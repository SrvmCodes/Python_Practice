def NNS(n):
    if n<=1:
        return (n)
    else:
        return((n)+NNS(n-1))
    
n= int(input("Enter a num here: "))
if n <= 0:
    print("Enter a positive num please!!")
else:
    print("Sum of given natural num is: ", NNS(n))