num = input("Enter numbers (comma separated): ")
mylist = [int(x.strip()) for x in num.split(",")]

positive=negative=zero=0
for n in mylist:
    if n > 0:
        positive += 1
    elif n<0:
        negative +=1
    else:
        zero+=1

print(f"Positive: {positive}")
print(f"Negative: {negative}")
print(f"zero :{zero}")