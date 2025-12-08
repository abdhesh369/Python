numbers = input("Enter numbers (comma-separated): ")
num_list = [int(x.strip()) for x in numbers.split(",")]
new_list = []

for i in range(len(num_list)):
    for j in range(i+1, len(num_list)):
        if num_list[i] == num_list[j] and num_list[i] not in new_list:
            new_list.append(num_list[i])

print(new_list)