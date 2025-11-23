import math


def isprime(num):
    if num <= 0:
        print("invalid number or enter positive number")
    elif num == 1:
        print("it is not prime")
        return False

    else:
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return False

    return True


number = int(input("enter a number\n"))
if isprime(number):
    print("It is prime number")
else:
    print("it is not prime number")
