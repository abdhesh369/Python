def filter_greater(numbers, limit):
    greater_list = []
    for num in numbers:
        if num >= 15:
            greater_list.append(num)
    return greater_list


numbers = [10, 25, 5,35,56,78,11,23,456,7,35,32, 40, 12]
result = filter_greater(numbers,15)
print(result)
