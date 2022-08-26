def longest(a1, a2):
    count = []
    res = ""
    for character in a1:
        if character not in count:
            count.append(character)
        else:
            continue
    for character in a2:
        if character not in count:
            count.append(character)
        else:
            continue
    count.sort()
    for new_str in count:
        res = res + new_str
    return res

print(longest("aretheyhere", "yestheyarehere"))