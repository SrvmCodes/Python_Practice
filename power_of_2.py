nterms = int(input("Enter number of terms here: "))

result = list(map(lambda x : 2**x, range(nterms+1)))

#print result in the form of list[]
# print(result)  

for i in range(nterms+1):
    print("The value of 2 to the power",i,"is",result[i])
