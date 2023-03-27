def romanToInt(s: str) -> int:
    mp = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    num = 0
    for idx, ch in enumerate(s):
        if ch in mp:
            num += mp[ch]
        if idx > 0 and mp[s[idx]] > mp[s[idx-1]]:
            num -= 2*mp[s[idx-1]]

    return num


# print(romanToInt('MCMXCIV'))