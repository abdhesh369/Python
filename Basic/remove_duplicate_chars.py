def remove_duplicates(str1):
    result = ""
    for char in str1:
        if char not in result:
            result += char
    return result


text1 = str(input("enter a text:\n"))
text2 = remove_duplicates(text1)
print(text2)
