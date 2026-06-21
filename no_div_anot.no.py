# USING FOR LOOP

# print('Numbers divisible by 13 are: ')
# for i in range (1, 100):
#     if i % 13 == 0:
#         print(i)
 

# USING LAMBDA() & FILTER()
num = int(input("Enter a number to find its divisible: "))
l = [12, 13, 14, 15, 18, 21, 45, 32, 42, 11, 64, 73, 81]
result = list(filter(lambda x : x % num == 0, l))

print("Num divisible:", result)


