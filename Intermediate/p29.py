numbers = input("Enter numbers (comma-separated): ")
num_list = [int(x.strip()) for x in numbers.split(",")]
reversed_list = []
for i in range(len(num_list) - 1, -1, -1):
    reversed_list.append(num_list[i])

print("Reversed list:", reversed_list)
