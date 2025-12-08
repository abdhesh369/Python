
num = input("Enter a list of numbers (comma separated): ")
newlist = [int(x.strip()) for x in num.split(",")]
list1 = []
for x in newlist:
    y = 0
    while x > 0:
        y += x % 10
        x = x//10
    list1.append(y)
print(list1)
