# 0,1,1,2,3,5,8,13,21
# Febonacci seq using for loop
# 1st and 2nd num must be 0 and 1
a = 0
b = 1
num = int(input("Enter num to obtain its fibonacci series: "))
if num == 1:
    print(a)
else:
    print(a)
    print(b)
    for i in range(2, num):
        c = a+b
        a = b
        b = c
        print(c)
        
