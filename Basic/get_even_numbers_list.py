def get_even(numbers):
    even_list = []
    for num in numbers:
        if num % 2 == 0:
            even_list.append(num)
    return even_list


x = [1, 2, 3, 4, 5, 6]
result = get_even(x)
print(result)
