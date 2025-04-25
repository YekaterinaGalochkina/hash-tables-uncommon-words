def uncommon_from_sentences(s1, s2):
    list1 = s1.split()
    list2 = s2.split()

    list = list1 + list2

    unique_words = []

    for word in list:
        if list.count(word) == 1:
            unique_words.append(word)
            
    return unique_words

print(uncommon_from_sentences("this apple is sweet","this apple is sour")) # expected = ["sweet", "sour"]


def uncommon_from_sentences(s1, s2):
    list1 = s1.split()
    list2 = s2.split()

    all_words = list1 + list2

    word_freq = {}  # hash table

    for word in all_words:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1

    unique_words = []
    for word in word_freq:
        if word_freq[word] == 1:
            unique_words.append(word)

    return unique_words

print(uncommon_from_sentences("this apple is sweet","this apple is sour")) # expected = ["sweet", "sour"]
