# # USING DICTIONART
# =============================================
a = "I am Saurav Singh from Hyderabad"
vowels = "aeiou"
a = a.casefold()
count = {}.fromkeys(vowels, 0)
print(count)

for char in a:
    if char in count:
        count[char] += 1
        
print(count)

# USING LIST AND DICTIONARY COMPREHENSION
# ================================================
# 
# a = "I am SauravSingh from Bihar"
# vowels = "aeiou"
# a = a.casefold()
# count = {key:sum([1 for char in a if char == key])for key in vowels}
# print(count)