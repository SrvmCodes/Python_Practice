def DecToBin(n):
    if n>1:
        DecToBin(n//2)
    print(n%2, end = "")

print("The binary of the given num is: ")
DecToBin(11)