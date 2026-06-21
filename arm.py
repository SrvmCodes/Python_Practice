num = int(input("Ente your num here: "))
sum = 0
temp = num
while temp>0:
    digit = temp%10
    cube = digit**3
    sum = cube+sum
    temp = temp//10
if sum == num:
    print("Armstrong Number")
else:
    print("Not Armstrong")