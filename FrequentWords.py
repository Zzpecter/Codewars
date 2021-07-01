def clean_text(text):
    clean = False
    while not clean:
        found_special = False
        for letter in text:
            if not letter.isalpha() and letter != " " and letter != r"'":
                text = text.replace(letter, ' ')
                found_special = True
                break
        if not found_special:
            clean = True
    return text


def clean_words(word_list):
    clean_word_list = []
    for word in word_list:
        for letter in word:
            if letter.isalpha():
                clean_word_list.append(word)
                break
    return clean_word_list


def get_frequencies(word_list):
    word_frequencies = {}
    for word in word_list:
        if word not in word_frequencies:
            word_frequencies[word] = 0
        word_frequencies[word] += 1
    return dict(sorted(word_frequencies.items(), key=lambda item: item[1], reverse=True))


def top_3_words(text):
    print(text)
    word_list = clean_text(text).lower().split(' ')
    word_list = clean_words(word_list)
    word_frequencies = get_frequencies(word_list)
    most_frequent_words = list(word_frequencies.keys())

    if len(most_frequent_words) > 3:
        most_frequent_words = most_frequent_words[:3]
    return most_frequent_words
print(top_3_words(r"ckkh'P_?ckkh'P-YNkJcbe;/ !.YNkJcbe:! ckkh'P:!_;_ckkh'P!?!YNkJcbe/ckkh'P ,_ ,ckkh'P/YNkJcbe/!??YNkJcbe/ckkh'P;:-ckkh'P,!?!YNkJcbe:.,?YNkJcbe?,,:ckkh'P-?/;,ckkh'P_!/;!ckkh'P?YNkJcbe:/:ckkh'P_YNkJcbe/.ckkh'P?.!YNkJcbe, YNkJcbe:ckkh'P_.!?-ckkh'P_:ckkh'P_YNkJcbe_/!YNkJcbe;ckkh'P/.YNkJcbe!ckkh'P -;:"))