def p(n):
    if n == 1:
        print(n)
        return
    p(n - 1)
    print(n)


def p(n):
    if n == 1:
        print(n)
        return
    print(n)
    p(n - 1)


p(10)