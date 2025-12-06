num = input("Enter a list of numbers (comma separated): ")
mylist = num.split(",")
newlist=[int(x.strip()) for x in mylist]
sum=0
for x in newlist:
    sum+=x
print(sum)