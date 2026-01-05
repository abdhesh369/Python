num = input("Enter a list of numbers (comma separated): ")
mylist = num.split(",")
newlist = [int(x.strip()) for x in mylist]
newlist1 = []
for x in newlist:
    if x >= 10:
        newlist1.append(x)
print(newlist1)
