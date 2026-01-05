numbers = input("Enter numbers (comma-separated): ")

num_list = [int(x.strip()) for x in numbers.split(",")]

total = 0
count = 0
for n in num_list:
    total += n
    count += 1

average = total / count if count != 0 else 0

print("Average of the numbers:", average)
