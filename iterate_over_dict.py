friends = {"john":"Duck", "Mohit":"Raj", "Srv":"Singh"}
print(friends)

#Using  .items
for key, value in friends.items():
    print(key,":",value)

# Using  key
for key in friends:
    print(key,"-",friends[key])

# Using  "key" and "value" individually
for key in friends.keys():
    print (key)

for value in friends.values():
    print(value)