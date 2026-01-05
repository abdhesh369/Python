numbers = input("Enter numbers (comma-separated): ")
arr = [int(x.strip()) for x in numbers.split(",") if x.strip()]

n = len(arr)
if n > 1:
    last = arr[n - 1]
    for i in range(n - 1, 0, -1):
        arr[i] = arr[i - 1]
    arr[0] = last

print("Right rotated list:", arr)