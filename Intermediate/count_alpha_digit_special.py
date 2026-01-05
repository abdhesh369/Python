text = input("Enter a string: ")

alpaha_count = 0
digit_count = 0
special_count = 0

for char in text:
    if char.isalpha():
        alpaha_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        special_count+= 1

print("Alphabets:", alpaha_count)
print("Digits:", digit_count)
print("special Characters:", special_count)