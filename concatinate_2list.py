# Using____ '+' Operator
l1 = [1,2,4,6,"K", "L", "J"]
l2 = [5,3,2,7,9,"S", "J", "M"]
l3 = l1+l2
print(l3)

# Using____ set() -> Unique values
l3 = list(set(l1+l2))
print(l3)

# Using____ extend()
l1.extend(l2)
print(l1)