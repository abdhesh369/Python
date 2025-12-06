num = input("Enter a list of numbers (comma separated): ")
mylist = num.split(",")
newlist=[int(x.strip()) for x in mylist]
sqlist=[x**0.5 for x in newlist]
print(sqlist)