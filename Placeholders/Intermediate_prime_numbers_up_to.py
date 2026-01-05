num = int(input("Enter a number: "))
primes = []

for i in range(2, num):   
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(i)

print("Prime numbers up to", num, ":", primes)