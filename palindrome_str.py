# a = input("Enter a word here: ")
# rev = a[::-1]
# if a == rev:
#     print("Palindrome")
# else:
#     print("Not palindrome")

num = int(input("Enter a num here: "))
temp = num
rev = 0
while num>0:
    digit = num%10 
    rev = rev*10+digit
    num = num//10

if temp == rev:
    print("Palindrome Number")

else:
    print("Not Palindrome")