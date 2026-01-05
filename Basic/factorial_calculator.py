# def factorial(n):
#     if n > 0:
#         return n * factorial(n-1)
#     elif n == 0:
#         return 1
#     else:
#         return "invalid"

# number = int(input("Enter a number\n"))
# y = factorial(number)
# print(f"factorial of {number} is {y}")


def factorialof(n):
    factorial=1
    for i in range(1, n+1):
        factorial *= i
    return factorial


number = int(input("enter a number\n"))
y = factorialof(number)
print(y)
