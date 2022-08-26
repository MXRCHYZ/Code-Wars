def anagrams(word, words):
    checker = {word: {}}
    res = []
    for letter in word:
        checker[word].setdefault(letter, 0)
        checker[word][letter] += 1
    for ana_words in words:
        checker[ana_words] = {}
        for ana_letter in ana_words:
            checker[ana_words].setdefault(ana_letter, 0)
            checker[ana_words][ana_letter] += 1
        if checker[word] == checker[ana_words]:
            res.append(ana_words)
    return res


if __name__ == "__main__":
    print(anagrams("abba", ["aabb", "abcd"]))