def isValid(s: str) -> bool:
    stack = []
    pair = {"[": "]", "{": "}", "(": ")"}
    for ch in s:
        if ch in pair:
            stack.append(ch)
        else:
            val = stack.pop()
            if pair.get(val, None) != ch:
                return False

    return False if stack else True


s = "()"
print(isValid(s))
