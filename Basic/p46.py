def char_frequency(text):
    text = text.lower()
    freq = {}

    for ch in text:
        if ch == " ":
            continue
        if ch in freq:
            freq[ch] += 1   

        else:
            freq[ch] = 1    
    return freq


print(char_frequency("Hello World"))
print(char_frequency("Python Programming"))
