a = "Have not seen any part of Harry Potter"
w = a.split() #Split into comma separated values

for i in range(len(w)):
    w[i] = w[i].lower()

w.sort()
print(w)

for i in w:    
    print(i)