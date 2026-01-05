text = input("Enter text (comma-separated): ")
text1 = [(x.strip()) for x in text.split(",")]
palindrome = []
for word in text1:
    reversed_list=""
    for i in range(len(word) - 1, -1, -1):
        reversed_list+=word[i]
    if word == reversed_list:
        palindrome.append(word)

print("Palindrome list:", palindrome)