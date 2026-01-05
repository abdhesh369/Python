def rev_number(num):
    rev = 0
    if num > 0:
        while num > 0:
            x = num % 10
            rev = rev*10+x
            num //= 10
    return rev


number = int(input("enter a number:\n"))
y = rev_number(number)
print(y)
