def repeatedStringMatch(a: str, b: str) -> int:
    temp = a
    for i in range(1, len(b)//len(a)+3):
        if b in temp:
            return i
        else:
            temp += a

    return -1


print(repeatedStringMatch("abc", "cabcabca"))
