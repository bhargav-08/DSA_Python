def scramble(a, b):

    if len(a) != len(b):
        return False

    n = len(a)

    if not n:
        return True
    if a == b:
        return True

    if a + b in cache:
        return cache[a + b]

    length = len(a)

    for i in range(1, length):
        if (scramble(a[:i], b[length - i:]) and scramble(a[i:], b[:n - i])):
            cache[a + b] = True
            return True

        if (scramble(a[:i], b[:i]) and scramble(a[i:], b[i:])):
            cache[a + b] = True
            return True

    cache[a + b] = False
    return False


cache = {}
a = "coder"
b = "ocred"
print(scramble(a, b))
