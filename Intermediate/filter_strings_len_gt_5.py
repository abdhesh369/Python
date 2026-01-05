input_strings = input("Enter strings separated by commas: ")
string_list = [s.strip() for s in input_strings.split(",")]
filtered_list = [s for s in string_list if len(s) > 5]
print("Strings with length greater than 5:", filtered_list)