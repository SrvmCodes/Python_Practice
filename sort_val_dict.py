marks = {"Jon":26, "Lisa":35, "Sid":22, "Mohit":40}
print(marks)

# Sorting Dict Based on values
sort_val = sorted(marks.items(), key = lambda x: x[1])
for i in sort_val:
    print(i)

# Sorting only based on value
sort_val = sorted(marks.values())
print(sort_val)