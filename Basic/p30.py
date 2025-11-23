def fibonacci(num):
    a, b = 0, 1
    print(a)
    if num > 1:
        print(b)
        for _ in range(2, num+1):
            c = a+b
            print(c)
            a,b=b,c


number = int(input("Enteer a number\n"))
y = fibonacci(number)
print(y)
