# Factorial means 
# 5! = 5*4*3*2*1 = 120
# num = int(input("Enter a num: "))
# fact = 1
# if num<0:
#     print("Fact dosen't exists")
# if num==0:
#     print("Fact of 0 is", 1)
# if num>0:
#     for i in range (1, num+1):
#         fact = fact*i
# print("Fact of given num is: ", fact)


# Using Recursion Method
def fact(a):
    if a == 0:
        return 1
    else:
        return ((a)*fact(a-1))
num = int(input("Enter your num: "))
result = fact(num)
print("Fact of this given num is: ", result)