num = input("Enter a list of numbers (comma separated): ")
newlist=[int(x.strip()) for x in num.split(",")]
odd=[]
even=[]
for x in newlist:
    if x%2==0:
        even.append(x)
    else:
        odd.append(x)    

print(f"Even: {even}")
print(f"odd: {odd}")