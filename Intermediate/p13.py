num = input("Enter a list of numbers (comma separated): ")
mylist = num.split(",")
mylist = [int(x.strip()) for x in mylist]
x = max(mylist)
y = min(mylist)

print(f"Minimum: {y} and Maximum: {x}")