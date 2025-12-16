numbers = input("Enter numbers (comma-separated): ")
arr = [int(x.strip()) for x in numbers.split(",") if x.strip()]

n = len(arr)
if n > 1:
    first = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = first

print(arr)