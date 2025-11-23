def is_armstrong(number):
    digits = str(number)
    length = len(digits)
    total = 0

    for d in digits:
        total += int(d)**length

    return total == number

num=int(input("enter a number\n"))
if  is_armstrong(num):
    print(f"{num} is armstrong")
else:
    print(f"{num} is not armstrong")