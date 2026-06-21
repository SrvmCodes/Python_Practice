import keyword
# Print all the keywords present in Python
print(keyword.kwlist)
# ==============================================
word = ["break","three","john", "continue", "lambda", "peter", "global", "number"]
for i in range (len(word)):
    if keyword.iskeyword(word[i]):
        print(word[i], "is a keyword of python")
    else:
        print(word[i], "is not a keyword in python")
