num = int(input("Enter your num here: "))
try:
    word= input("Enter your string value here:")
    print(num+word)
except(ValueError, TypeError) as a:
    print(a)