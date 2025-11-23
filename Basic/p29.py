def add(num):
    x = 0
    if num > 0:
        while num > 0:
            y = num % 10
            x += y
            num  //= 10
    return x


number = int(input("enter a number\n"))
sum = add(number)
print(sum)
