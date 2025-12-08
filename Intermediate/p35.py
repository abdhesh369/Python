numbers = input("Enter numbers (comma-separated): ")
num_list = [int(x.strip()) for x in numbers.split(",")]
count = 0
for i in num_list:
    is_prime = True
    for j in range(2, int(i**0.5) + 1):
        if i % j == 0:
            is_prime = False
            break
    if is_prime:
        count += 1

print("The number of prime is:", count)
