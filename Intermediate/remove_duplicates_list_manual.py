numbers = input("Enter numbers (comma-separated): ")
num_list = [int(x.strip()) for x in numbers.split(",")]
new_list = []
for i in num_list:
    if i not in new_list:
        new_list.append(i)
print(new_list)
