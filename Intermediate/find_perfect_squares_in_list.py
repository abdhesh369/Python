
num = input("Enter a list of numbers (comma separated): ")
mylist = num.split(",")
newlist=[int(x.strip()) for x in mylist]
sqlist=[x for x in newlist if int(x**0.5)**2==x]
print(sqlist)