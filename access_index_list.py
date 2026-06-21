# USING ENUMERATE METHOD
# l = [12, 23, 24, 34, 54, 15, 21, 64, 13]
# for index, value in enumerate(l, start=1):
#     print(index,":", value)

# WITHOUT USING ENUMERATE METHOD
l = [12, 23, 24, 34, 54]
for index in range (len(l)):
    value = l[index]
    print(index,value)