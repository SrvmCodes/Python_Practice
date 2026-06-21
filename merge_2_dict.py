dict1 ={"Amit" : 24, "Sonu" : 34}
dict2 ={"Sumit" : 14, "Sonu" : 44}
# USING Bar "|" Operator
print(dict1 | dict2)

# USING ** Operator
print({**dict1, **dict2})

# USING copy() & update() Method
dict1 ={"Amit" : 24, "Sonu" : 34}
dict2 ={"Sumit" : 14, "Sonu" : 44}
dict3 = dict2.copy()
dict3.update(dict1)
print(dict3)