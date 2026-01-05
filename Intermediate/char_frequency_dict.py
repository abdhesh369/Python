text = input("Enter a string: ")
mydir = {}
for char in text:
    if char in mydir:
        mydir[char] += 1
    else:
        mydir[char] = 1    
print(mydir)
