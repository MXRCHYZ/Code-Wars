def find_missing_letter(chars):
    """h"""
    test_lower = 'abcdefghijklmnopqrstuvwxyz'
    test_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    startIndex = 0
    endIndex = 0
    if chars[0] in test_lower:
        startIndex = test_lower.index(chars[0])
        endIndex = test_lower.index(chars[-1])
        for letter in test_lower[startIndex:endIndex+1]:
            if letter not in chars:
                print(letter)
                break
            else:
                continue
    else:
        startIndex = test_upper.index(chars[0])
        endIndex = test_upper.index(chars[-1])
        for letter in test_upper[startIndex:endIndex+1]:
            if letter not in chars:
                print(letter)
                break
            else:
                continue

find_missing_letter(['a','b','c','d','f'])