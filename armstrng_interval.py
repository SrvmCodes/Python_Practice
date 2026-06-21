lower = int(input("Enter the lower num: "))
upper = int(input("Enter the upper num: "))
for num in range (lower, upper+1):
    order = len(str(num)) 
    sum = 0
    temp = num
    while temp>0:
        digit = temp%10
        cube = digit**3
        sum = sum+cube
        temp = temp // 10
    if num == sum:
        print(num)