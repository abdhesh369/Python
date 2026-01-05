numbers = input("Enter numbers (comma-separated): ")

num_list = [int(x.strip()) for x in numbers.split(",")]

most_frequent = None
highest_freq = 0

for i in range(len(num_list)):
    current_num = num_list[i]
    freq = 0
    
    for j in range(len(num_list)):
        if num_list[j] == current_num:
            freq += 1
    
    if freq > highest_freq:
        highest_freq = freq
        most_frequent = current_num

print("Most frequent number:", most_frequent)