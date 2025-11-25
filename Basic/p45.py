def word_list(sentence):
    text_list = []
    in_word = False
    current_word = ""

    for ch in sentence:
        if ch != " ":
            if not in_word:
                in_word = True
                current_word = ch
            else:
                current_word += ch
        else:
            if in_word:
                text_list.append(current_word)
                in_word = False
                current_word = ""

    if in_word:
        text_list.append(current_word)

    return text_list


print(word_list("hello world"))
print(word_list(" hello python world "))
print(word_list("   multiple   spaces   "))
