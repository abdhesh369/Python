def count_vol(text):
    vowels = "aeiou"
    count=0
    text1=text.lower()
    for ch in text1:
        if  ch in vowels:
            count+=1
    return count

txt=str(input("enter text:\n"))
y=count_vol(txt)
print(y)