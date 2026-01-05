numbers = input("Enter numbers (comma-separated): ")

num_list = [int(x.strip()) for x in numbers.split(",")]

result = []
zero_count = 0

for n in num_list:
    if n == 0:
        zero_count += 1
    else:
        result.append(n)

result.extend([0] * zero_count)

print("List after moving zeros to the end:", result)
