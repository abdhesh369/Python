def count_vowels(text):
    count=0
    x=text.lower()
    for i in x:
        if i in "aeiou":
            count +=1
    return count 


print (count_vowels("Hello world"))