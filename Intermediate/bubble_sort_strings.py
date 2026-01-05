input_strings = input("Enter strings separated by commas: ")
words = [s.strip() for s in input_strings.split(",")]
n = len(words)
for i in range(n):
    for j in range(0, n-i-1):
        if words[j] > words[j+1]:
            words[j], words[j+1] = words[j+1], words[j]
print(words)