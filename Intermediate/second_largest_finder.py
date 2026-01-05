num = input("Enter numbers (comma separated): ")
mylist = [int(x.strip()) for x in num.split(",")]

first = second = float('-inf')

for n in mylist:
    if n > first:
        second = first
        first = n
    elif n > second and n != first:
        second = n

if second == float('-inf'):
    print("No second largest (need two distinct numbers)")
else:
    print("Second largest:", second)