def toreversed(xyz):
    x = xyz.lower().replace(" ", "")
    return x[::-1]


y = input("enter a word\n")


if toreversed(y) == y:
    print("palindrome")
else:
    print("Not palindrome")
