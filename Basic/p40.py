def count_even(numbers):
    count = 0
    for i in numbers:
        if i % 2 == 0:
            count += 1
    return count


x=count_even([1,2,3,4,5,6,7])
print(x)