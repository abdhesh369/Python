def char_frequency(text):
    freq = {}
    for ch in text.lower():
        if ch.isalpha():
            freq[ch] = freq.get(ch, 0) + 1
    return freq

def is_anagram(str1, str2):
    return char_frequency(str1) == char_frequency(str2)


print(is_anagram("listen", "silent"))
print(is_anagram("Hello", "Ole lh"))
print(is_anagram("Python", "Java"))
print(is_anagram("School master", "The classroom"))
