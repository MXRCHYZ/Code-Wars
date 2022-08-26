def is_pangram(s):
    check = "abcdefghijklmnopqrstuvwxyz"
    pan = {}
    for c in check:
        if c in s.lower():
            pan.setdefault(c, 0)
    
    return len(pan.keys()) == 26

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))