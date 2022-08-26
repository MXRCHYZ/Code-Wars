def find_outlier(integers):
    dict = {}
    even = 0
    odd = 0
    for i in integers:
        dict.setdefault(i, i % 2)
    for v in dict.values():
        if v == 0:
            even += 1
        else:
            odd += 1
    if even > odd:       
        for key, value in dict.items():
            if value != 0:
                return key
            else:
                continue
    else:
        for key, value in dict.items():
            if value == 0:
                return key
            else:
                continue
        
print(find_outlier([2, 4, 6, 8, 10, 3]))