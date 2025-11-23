def are_anagrams(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    return sorted(str1) == sorted(str2)


text1 = str(input("enter a sentance\n"))
text2 = str(input("enter a sentance\n"))
if are_anagrams(text1, text2):
    print("anagrams")
else:
    print("not anagrams")
