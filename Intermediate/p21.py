input_strings = input("Enter strings separated by commas: ")

string_list = [s.strip() for s in input_strings.split(",")]
longest_word = ""

for word in string_list:
    if len(word) > len(longest_word):
        longest_word = word

print("Longest word:", longest_word)
