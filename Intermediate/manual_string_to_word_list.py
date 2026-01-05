text = input("Enter text: ")
text1 = []
text2 = ""
for i in range(len(text)):
    if text[i] == " ":
        text1.append(text2)
        text2=""
    else:
        text2 += text[i]
if text2:
    text1.append(text2)
print(text1)