import re

text = "My phone is 980-709-9072 and my pin is 1234"
digits = re.findall(r"\d", text)
print(digits)
words = re.findall(r"\b[A-Za-z]+\b", text)
print(words)
five_letter_words = re.findall(r"\b[A-Za-z]{5}\b", text)
print(five_letter_words)