def solution(roman):
    res = 0
    for r in roman:
        if "M" == r:
            res += 1000
        elif "D" == r:
            res += 500
        elif "C" == r:
            res += 100
        elif "L" == r:
            res += 50
        elif "X" == r:
            res += 10
        elif "V" == r:
            res += 5
        elif "I" == r:
            res += 1
    if "IV" in roman:
        res -= 2
    if "IX" in roman:
        res -= 2
    if "CM" in roman:
        res -= 200
    if "CX" in roman:
        res -= 20
    return res

print(solution("MMMCCXCIX"))