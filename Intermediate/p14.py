num = input("Enter a list of numbers (comma separated): ")
mylist = num.split(",")
newlist=set([int(x.strip()) for x in mylist])
nwelist1 = list(newlist)

print(nwelist1)